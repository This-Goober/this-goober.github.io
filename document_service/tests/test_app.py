from fastapi.testclient import TestClient

from doc_service.app import app, settings


def test_bearer_authentication_is_declared_and_enforced(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("DOCS_API_KEY", "test-secret")
    settings.cache_clear()

    try:
        client = TestClient(app)
        assert client.get("/health").status_code == 401
        assert client.get("/health", headers={"Authorization": "Bearer wrong"}).status_code == 401
        assert client.get("/health", headers={"Authorization": "Bearer test-secret"}).status_code == 200

        schema = client.get(
            "/openapi.json", headers={"Authorization": "Bearer test-secret"}
        ).json()
        assert schema["components"]["securitySchemes"]["HTTPBearer"]["scheme"] == "bearer"
        assert schema["paths"]["/search"]["post"]["security"] == [{"HTTPBearer": []}]
        document_ids = schema["components"]["schemas"]["SearchRequest"]["properties"]["document_ids"]
        assert document_ids["default"] == []
    finally:
        settings.cache_clear()
