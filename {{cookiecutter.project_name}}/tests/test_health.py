"""Health check tests."""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_health_check():
    """Test health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_readiness():
    """Test readiness endpoint."""
    response = client.get("/api/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_version():
    """Test version endpoint."""
    response = client.get("/api/version")
    assert response.status_code == 200
    assert "version" in response.json()