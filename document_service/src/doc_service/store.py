from __future__ import annotations

import hashlib
import sqlite3
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from pypdf import PdfReader


@dataclass(frozen=True)
class Chunk:
    page: int
    ordinal: int
    text: str


def chunk_pdf(path: Path, size: int, overlap: int) -> list[Chunk]:
    if overlap >= size:
        raise ValueError("chunk overlap must be smaller than chunk size")
    result: list[Chunk] = []
    ordinal = 0
    for page_number, page in enumerate(PdfReader(path).pages, start=1):
        words = (page.extract_text() or "").split()
        start = 0
        while start < len(words):
            text = " ".join(words[start : start + size])
            if text.strip():
                result.append(Chunk(page_number, ordinal, text))
                ordinal += 1
            start += size - overlap
    return result


class Store:
    def __init__(self, db_path: Path, embedder):
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(db_path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.embedder = embedder
        self.db.executescript(
            """
            PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS documents (
              id INTEGER PRIMARY KEY, name TEXT NOT NULL, sha256 TEXT NOT NULL UNIQUE,
              pages INTEGER NOT NULL, chunks INTEGER NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS chunks (
              id INTEGER PRIMARY KEY, document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
              page INTEGER NOT NULL, ordinal INTEGER NOT NULL, text TEXT NOT NULL,
              embedding BLOB NOT NULL
            );
            CREATE INDEX IF NOT EXISTS chunks_document_id ON chunks(document_id);
            """
        )
        self.db.execute("PRAGMA foreign_keys=ON")

    def ingest(self, path: Path, name: str, chunk_words: int, overlap: int) -> dict:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        existing = self.db.execute("SELECT * FROM documents WHERE sha256=?", (digest,)).fetchone()
        if existing:
            return dict(existing) | {"already_indexed": True}
        chunks = chunk_pdf(path, chunk_words, overlap)
        if not chunks:
            raise ValueError("PDF contains no extractable text (scanned PDFs need OCR first)")
        vectors = list(self.embedder.embed([chunk.text for chunk in chunks]))
        pages = max(chunk.page for chunk in chunks)
        with self.db:
            cursor = self.db.execute(
                "INSERT INTO documents(name, sha256, pages, chunks) VALUES (?, ?, ?, ?)",
                (name, digest, pages, len(chunks)),
            )
            document_id = cursor.lastrowid
            self.db.executemany(
                "INSERT INTO chunks(document_id,page,ordinal,text,embedding) VALUES (?,?,?,?,?)",
                [
                    (document_id, chunk.page, chunk.ordinal, chunk.text, np.asarray(vector, dtype=np.float32).tobytes())
                    for chunk, vector in zip(chunks, vectors, strict=True)
                ],
            )
        return {"id": document_id, "name": name, "sha256": digest, "pages": pages, "chunks": len(chunks), "already_indexed": False}

    def search(self, query: str, limit: int, document_ids: list[int] | None = None) -> list[dict]:
        sql = "SELECT c.*, d.name FROM chunks c JOIN documents d ON d.id=c.document_id"
        params: list[int] = []
        if document_ids:
            sql += f" WHERE c.document_id IN ({','.join('?' for _ in document_ids)})"
            params.extend(document_ids)
        rows = self.db.execute(sql, params).fetchall()
        if not rows:
            return []
        query_vector = np.asarray(next(iter(self.embedder.query_embed(query))), dtype=np.float32)
        matrix = np.stack([np.frombuffer(row["embedding"], dtype=np.float32) for row in rows])
        # FastEmbed's supported retrieval models emit normalized vectors; normalize again for custom embedders/tests.
        matrix /= np.maximum(np.linalg.norm(matrix, axis=1, keepdims=True), 1e-12)
        query_vector /= max(float(np.linalg.norm(query_vector)), 1e-12)
        scores = matrix @ query_vector
        indices = np.argsort(scores)[::-1][:limit]
        return [
            {
                "chunk_id": rows[i]["id"], "document_id": rows[i]["document_id"],
                "document": rows[i]["name"], "page": rows[i]["page"],
                "score": round(float(scores[i]), 6), "text": rows[i]["text"],
            }
            for i in indices
        ]

    def documents(self) -> list[dict]:
        return [dict(row) for row in self.db.execute("SELECT * FROM documents ORDER BY id")]

    def delete(self, document_id: int) -> bool:
        with self.db:
            cursor = self.db.execute("DELETE FROM documents WHERE id=?", (document_id,))
        return cursor.rowcount > 0
