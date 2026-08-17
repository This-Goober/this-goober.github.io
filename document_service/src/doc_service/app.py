from __future__ import annotations

import hmac
import os
import tempfile
from functools import lru_cache
from pathlib import Path

from fastapi import Depends, FastAPI, File, Header, HTTPException, UploadFile
from fastembed import TextEmbedding
from pydantic import BaseModel, Field

from .config import Settings
from .store import Store


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=4000)
    limit: int = Field(default=8, ge=1, le=50)
    document_ids: list[int] | None = None


@lru_cache
def settings() -> Settings:
    return Settings()


@lru_cache
def store() -> Store:
    config = settings()
    return Store(config.data_dir / "documents.sqlite3", TextEmbedding(model_name=config.model))


def authorize(authorization: str | None = Header(default=None)) -> None:
    key = settings().api_key
    if key and (not authorization or not hmac.compare_digest(authorization, f"Bearer {key}")):
        raise HTTPException(401, "missing or invalid bearer token")


app = FastAPI(title="Local Document Search", version="0.1.0", dependencies=[Depends(authorize)])


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model": settings().model}


@app.get("/documents")
def list_documents() -> list[dict]:
    return store().documents()


@app.post("/documents")
async def add_document(file: UploadFile = File(...)) -> dict:
    if file.content_type not in {"application/pdf", "application/octet-stream"}:
        raise HTTPException(415, "only PDF uploads are accepted")
    config = settings()
    content = await file.read(config.max_upload_mb * 1024 * 1024 + 1)
    if len(content) > config.max_upload_mb * 1024 * 1024:
        raise HTTPException(413, f"file exceeds {config.max_upload_mb} MB")
    if not content.startswith(b"%PDF-"):
        raise HTTPException(400, "file is not a PDF")
    temp_path: Path | None = None
    try:
        descriptor, raw_path = tempfile.mkstemp(suffix=".pdf")
        os.close(descriptor)
        temp_path = Path(raw_path)
        temp_path.write_bytes(content)
        return store().ingest(temp_path, Path(file.filename or "document.pdf").name, config.chunk_words, config.chunk_overlap_words)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    finally:
        if temp_path:
            temp_path.unlink(missing_ok=True)


@app.delete("/documents/{document_id}")
def delete_document(document_id: int) -> dict:
    if not store().delete(document_id):
        raise HTTPException(404, "document not found")
    return {"deleted": document_id}


@app.post("/search")
def search(request: SearchRequest) -> dict:
    return {"results": store().search(request.query, request.limit, request.document_ids)}
