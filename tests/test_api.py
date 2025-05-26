# test_api.py

import pytest
from fastapi.testclient import TestClient
from app import app
from core.router import router
from core.intent_classifier import intent_classifier

client = TestClient(app)


class TestMizzleMateAPI:

    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "Healthy"
        assert "Mizzle Mate" in data["message"]

    def test_logs_endpoint(self):
        response = client.get("/logs")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_chat_endpoint_single_module(self, monkeypatch):
        # Patch the classify method on the instance
        monkeypatch.setattr(intent_classifier, "classify", lambda msg: ["ci_cd"])

        # Mock router to return a fixed response
        monkeypatch.setattr(
            router,
            "route_request",
            lambda mod, uid, msg: {
                "module": mod,
                "reply": "Test reply",
                "status": "success",
            },
        )

        payload = {"user_id": "testuser", "message": "Deploy my app"}
        response = client.post("/chat", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert data[0]["module"] == "ci_cd"
        assert data[0]["status"] == "success"

    def test_chat_endpoint_multiple_modules(self, monkeypatch):
        # Patch the classify method on the instance
        monkeypatch.setattr(
            intent_classifier, "classify", lambda msg: ["ci_cd", "logs"]
        )

        # Mock router to return a fixed response
        monkeypatch.setattr(
            router,
            "route_request",
            lambda mod, uid, msg: {
                "module": mod,
                "reply": f"Reply for {mod}",
                "status": "success",
            },
        )

        payload = {"user_id": "testuser", "message": "Deploy and show logs"}
        response = client.post("/chat", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        assert {d["module"] for d in data} == {"ci_cd", "logs"}
        assert all(d["status"] == "success" for d in data)


if __name__ == "__main__":
    pytest.main([__file__])
