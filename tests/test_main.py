import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app

client = TestClient(app)


def test_health_returns_200():
    r = client.get("/health")
    assert r.status_code == 200


def test_health_returns_json():
    r = client.get("/health")
    data = r.json()
    assert "status" in data
    assert data["status"] == "healthy"


def test_health_has_version():
    r = client.get("/health")
    assert "version" in r.json()


def test_items_requires_auth():
    r = client.get("/api/v1/items")
    assert r.status_code == 401


def test_items_with_bearer_token():
    r = client.get("/api/v1/items", headers={"Authorization": "Bearer test-token-123"})
    assert r.status_code == 200
    data = r.json()
    assert "items" in data
    assert isinstance(data["items"], list)


def test_items_with_bearer_returns_total():
    r = client.get("/api/v1/items", headers={"Authorization": "Bearer test-token-123"})
    data = r.json()
    assert "total" in data
    assert data["total"] == 0
