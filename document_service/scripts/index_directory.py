#!/usr/bin/env python3
"""Index every PDF in a directory using the service's configured store."""

from __future__ import annotations

import argparse
from pathlib import Path

from fastembed import TextEmbedding

from doc_service.config import Settings
from doc_service.store import Store


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="directory containing PDF files")
    args = parser.parse_args()

    directory = args.directory.expanduser().resolve()
    if not directory.is_dir():
        parser.error(f"not a directory: {directory}")

    paths = sorted(path for path in directory.iterdir() if path.is_file() and path.suffix.lower() == ".pdf")
    if not paths:
        print(f"No PDFs found in {directory}")
        return 0

    config = Settings()
    index = Store(config.data_dir / "documents.sqlite3", TextEmbedding(model_name=config.model))
    print(f"Found {len(paths)} PDF(s) in {directory}")

    failures = 0
    for path in paths:
        try:
            result = index.ingest(path, path.name, config.chunk_words, config.chunk_overlap_words)
            action = "skipped" if result["already_indexed"] else "indexed"
            print(f"{action}: {path.name} ({result['pages']} pages, {result['chunks']} chunks)")
        except Exception as exc:  # Continue so one malformed PDF does not stop a corpus run.
            failures += 1
            print(f"failed: {path.name}: {exc}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
