import numpy as np

from doc_service.store import Store


class FakeEmbedder:
    def _vector(self, text):
        text = text.lower()
        return np.array([text.count("apple"), text.count("ocean"), 0.1], dtype=np.float32)

    def embed(self, texts):
        return iter(self._vector(text) for text in texts)

    def query_embed(self, text):
        return iter([self._vector(text)])


def test_search_and_delete(tmp_path):
    store = Store(tmp_path / "test.sqlite3", FakeEmbedder())
    with store.db:
        document_id = store.db.execute(
            "INSERT INTO documents(name,sha256,pages,chunks) VALUES ('notes.pdf','hash',1,2)"
        ).lastrowid
        rows = [
            (document_id, 1, 0, "apple orchard", FakeEmbedder()._vector("apple orchard").tobytes()),
            (document_id, 1, 1, "deep ocean", FakeEmbedder()._vector("deep ocean").tobytes()),
        ]
        store.db.executemany("INSERT INTO chunks(document_id,page,ordinal,text,embedding) VALUES (?,?,?,?,?)", rows)
    assert store.search("apple", 1)[0]["text"] == "apple orchard"
    assert store.delete(document_id)
    assert store.documents() == []
