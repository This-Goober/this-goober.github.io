# Local PDF semantic search

A small, self-hosted semantic-search service for tens of PDFs and thousands of pages. It extracts PDF text with `pypdf`, makes overlapping page-local chunks, embeds them on CPU with FastEmbed's ONNX build of `BAAI/bge-small-en-v1.5`, and stores text and vectors in SQLite. Search uses exact cosine similarity with NumPy, which is simple and fast at this scale—there is no FAISS, ScaNN, or external vector database.

## What it provides

- Local CPU inference after the embedding model's initial download
- Exact page numbers in results because chunks never cross page boundaries
- Idempotent ingestion: identical PDFs are detected by SHA-256 and skipped
- Optional bearer-token authentication
- FastAPI endpoints for upload, listing, deletion, health, and search
- A standalone Python client suitable for an agent or Claude skill

## Quickstart

Prerequisites: Python 3.11 or newer. [`uv`](https://docs.astral.sh/uv/) is recommended, although a normal virtual environment also works.

```bash
cd document_service
uv sync --extra dev
cp .env.example .env
```

Open `.env`, replace `replace-with-a-long-random-secret` with the output of:

```bash
openssl rand -hex 32
```

Do not commit `.env`; it is ignored by Git. Start the service:

```bash
uv run uvicorn doc_service.app:app --host 127.0.0.1 --port 8000
```

The embedding model downloads on first use. In another terminal, load the key and check the service:

```bash
set -a
source .env
set +a

curl -H "Authorization: Bearer $DOCS_API_KEY" \
  http://127.0.0.1:8000/health
```

### Index a directory of PDFs

Index all top-level PDFs in a directory. Re-running the command safely skips files already present in the database.

```bash
uv run python scripts/index_directory.py ~/Documents/documents_corpus
```

Scanned or image-only PDFs are rejected because they need OCR first. Run a tool such as OCRmyPDF on those files, then retry.

List the indexed documents:

```bash
curl -H "Authorization: Bearer $DOCS_API_KEY" \
  http://127.0.0.1:8000/documents
```

Search all documents (omit `document_ids`; an unknown ID filters out every result):

```bash
curl -H "Authorization: Bearer $DOCS_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"query":"cognitive science at Harvard","limit":5}' \
  http://127.0.0.1:8000/search
```

### Python client

Copy `client.py` into an agent skill or import it locally:

```python
import os

from client import DocumentClient

docs = DocumentClient(
    base_url=os.environ.get("DOCS_BASE_URL", "http://127.0.0.1:8000"),
    api_key=os.environ["DOCS_API_KEY"],
)

for hit in docs.search("undergraduate research opportunities", limit=5):
    print(hit["document"], hit["page"], hit["score"], hit["text"])
```

Keep `DOCS_API_KEY` in the skill's secret/environment configuration, never in its source.

## API

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/health` | Liveness and configured embedding model |
| `POST` | `/documents` | Multipart PDF upload; identical files are not re-embedded |
| `GET` | `/documents` | List indexed documents and their IDs |
| `DELETE` | `/documents/{id}` | Remove a document and its chunks |
| `POST` | `/search` | Search by `query`, `limit`, and optional `document_ids` |

Interactive API documentation is available at <http://127.0.0.1:8000/docs> while the service is running.

## Configuration

Settings are environment variables or entries in `.env`:

| Variable | Default | Purpose |
|---|---:|---|
| `DOCS_DATA_DIR` | `./data` | Directory containing `documents.sqlite3` |
| `DOCS_MODEL` | `BAAI/bge-small-en-v1.5` | FastEmbed model name |
| `DOCS_CHUNK_WORDS` | `260` | Approximate chunk size |
| `DOCS_CHUNK_OVERLAP_WORDS` | `40` | Context shared by adjacent chunks |
| `DOCS_MAX_UPLOAD_MB` | `100` | Upload limit |
| `DOCS_API_KEY` | unset | Bearer token; required before internet exposure |

If the embedding model or chunk settings change, use a new `DOCS_DATA_DIR` and re-index. Existing vectors do not carry model-migration metadata.

## Start automatically on macOS

macOS uses `launchd` instead of systemd. The supplied LaunchAgent template starts the API at login and restarts it if it exits.

```bash
cd document_service
SERVICE_DIR="$(pwd -P)"
mkdir -p "$SERVICE_DIR/data" "$HOME/Library/LaunchAgents"
sed "s|__SERVICE_DIR__|$SERVICE_DIR|g" \
  com.thisgoober.document-service.plist.example \
  > "$HOME/Library/LaunchAgents/com.thisgoober.document-service.plist"
plutil -lint "$HOME/Library/LaunchAgents/com.thisgoober.document-service.plist"
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.thisgoober.document-service.plist"
```

If it was already loaded, apply a changed configuration with:

```bash
launchctl bootout "gui/$(id -u)/com.thisgoober.document-service"
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.thisgoober.document-service.plist"
```

Inspect status and logs:

```bash
launchctl print "gui/$(id -u)/com.thisgoober.document-service"
tail -f data/service.stderr.log
```

This is a per-user LaunchAgent, so it starts when that user logs in. A system LaunchDaemon is required if the service must start before login.

## Publish through Cloudflare Tunnel

Never expose an unauthenticated instance. Confirm `DOCS_API_KEY` is a strong random value before continuing. A named tunnel gives the client a stable HTTPS hostname without opening an inbound router port.

Install and authorize `cloudflared`:

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create document-service
cloudflared tunnel route dns document-service documents.example.com
```

The create command prints a tunnel UUID. Copy `cloudflared-config.yml.example` to `cloudflared-config.yml`, then replace:

- `__TUNNEL_ID__` with that UUID
- `__HOME__` with your absolute home directory
- `documents.example.com` with your hostname

Validate it and test in the foreground:

```bash
cloudflared tunnel --config cloudflared-config.yml ingress validate
cloudflared tunnel --config cloudflared-config.yml run document-service
```

To make the tunnel persistent on macOS, render and install its LaunchAgent:

```bash
SERVICE_DIR="$(pwd -P)"
CLOUDFLARED_BIN="$(command -v cloudflared)"
sed -e "s|__SERVICE_DIR__|$SERVICE_DIR|g" \
    -e "s|__CLOUDFLARED_BIN__|$CLOUDFLARED_BIN|g" \
  com.thisgoober.document-tunnel.plist.example \
  > "$HOME/Library/LaunchAgents/com.thisgoober.document-tunnel.plist"
plutil -lint "$HOME/Library/LaunchAgents/com.thisgoober.document-tunnel.plist"
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.thisgoober.document-tunnel.plist"
```

Verify that public requests without a token return `401`, then test with the token:

```bash
curl https://documents.example.com/health
curl -H "Authorization: Bearer $DOCS_API_KEY" \
  https://documents.example.com/health
```

The tunnel credential JSON under `~/.cloudflared`, the rendered configuration, `.env`, PDFs, model files, and SQLite data must remain private. They are excluded from this repository.

## Test

```bash
uv run pytest
```
