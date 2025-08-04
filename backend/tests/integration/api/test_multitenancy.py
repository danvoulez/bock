import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_tenant_isolation():
    idea_data_a = {"title": "Ideia A", "tenant_id": "tenant_a", "author_id": "p1"}
    idea_data_b = {"title": "Ideia B", "tenant_id": "tenant_b", "author_id": "p2"}

    ia = client.post("/ideas", json=idea_data_a, headers={"X-Tenant-ID": "tenant_a"}).json()
    ib = client.post("/ideas", json=idea_data_b, headers={"X-Tenant-ID": "tenant_b"}).json()

    # Listar ideias por tenant
    resp_a = client.get("/ideas", headers={"X-Tenant-ID": "tenant_a"})
    assert ia["title"] in resp_a.text
    assert ib["title"] not in resp_a.text

    resp_b = client.get("/ideas", headers={"X-Tenant-ID": "tenant_b"})
    assert ib["title"] in resp_b.text
    assert ia["title"] not in resp_b.text