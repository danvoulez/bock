import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_contract_creation_and_enforcement():
    contract_data = {
        "title": "Serviço de TI",
        "tenant_id": "tenant_001",
        "author_id": "person_001",
        "witness_id": "person_002",
        "value": 1000,
        "normal_consequence": "Pagamento efetuado",
        "questioning_procedure": "Questionar até 15 dias",
        "penalty_procedure": "Multa de 10%",
        "status": "active"
    }
    resp = client.post("/contracts", json=contract_data, headers={"X-Tenant-ID": "tenant_001"})
    assert resp.status_code == 200
    contract = resp.json()
    assert contract["status"] == "active"

    # Simular acionamento de penalidade
    enforcement_resp = client.post(f"/contracts/{contract['id']}/trigger", json={"action": "penalize"}, headers={"X-Tenant-ID": "tenant_001"})
    assert enforcement_resp.status_code == 200
    assert "Penalidade aplicada" in enforcement_resp.json()["message"]