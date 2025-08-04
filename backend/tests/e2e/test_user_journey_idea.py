import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_full_idea_flow():
    # Cria uma ideia
    idea_data = {
        "title": "Nova plataforma",
        "tenant_id": "tenant_002",
        "priority_data": {"initial": 6},
        "cost_data": {"value": 800},
        "author_id": "person_010"
    }
    resp = client.post("/ideas", json=idea_data, headers={"X-Tenant-ID": "tenant_002"})
    idea = resp.json()
    assert idea["title"] == "Nova plataforma"

    # Vota na ideia
    vote = {"score": 8, "voter_id": "person_011"}
    vote_resp = client.post(f"/ideas/{idea['id']}/vote", json=vote, headers={"X-Tenant-ID": "tenant_002"})
    assert "Voto registrado" in vote_resp.json()["message"]

    # Workflow: transforma em contrato se prioridade >= 7.5
    # (Simulado via regra do motor)
    # Adicione testes para a transição de workflow conforme regras do tenant