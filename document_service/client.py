from __future__ import annotations

from pathlib import Path

import httpx


class DocumentClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8000", api_key: str | None = None, timeout: float = 120):
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self.http = httpx.Client(base_url=base_url.rstrip("/"), headers=headers, timeout=timeout)

    def add_pdf(self, path: str | Path) -> dict:
        path = Path(path)
        with path.open("rb") as stream:
            response = self.http.post("/documents", files={"file": (path.name, stream, "application/pdf")})
        response.raise_for_status()
        return response.json()

    def search(self, query: str, limit: int = 8, document_ids: list[int] | None = None) -> list[dict]:
        response = self.http.post("/search", json={"query": query, "limit": limit, "document_ids": document_ids})
        response.raise_for_status()
        return response.json()["results"]

    def documents(self) -> list[dict]:
        response = self.http.get("/documents")
        response.raise_for_status()
        return response.json()

    def delete(self, document_id: int) -> None:
        response = self.http.delete(f"/documents/{document_id}")
        response.raise_for_status()
