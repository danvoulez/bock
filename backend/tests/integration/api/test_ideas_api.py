import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_vote_idea():
    idea_data = {
        "title": "Backup automático",
        "tenant_id": "tenant_001",
        "priority_data": {"initial": 8},
        "cost_data": {"value": 500},
        "author_id": "person_001"
    }
    resp = client.post("/ideas", json=idea_data, headers={"X-Tenant-ID": "tenant_001"})
    assert resp.status_code == 200
    idea = resp.json()
    assert idea["title"] == "Backup automático"

    vote = {"score": 9, "voter_id": "person_002"}
    vote_resp = client.post(f"/ideas/{idea['id']}/vote", json=vote, headers={"X-Tenant-ID": "tenant_001"})
    assert vote_resp.status_code == 200
    assert "Voto registrado" in vote_resp.json()["message"]