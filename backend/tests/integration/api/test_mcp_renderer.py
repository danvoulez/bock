import pytest
from mcp_bridge.renderer import MCPRenderer

def test_render_idea():
    idea = {
        "id": "i1", "title": "Backup", "current_priority": 8.7,
        "initial_priority": 8, "cost": 200, "vote_count": 17
    }
    renderer = MCPRenderer()
    output = renderer.render_idea(idea)
    assert "**Ideia #i1**" in output
    assert "Prioridade" in output

def test_render_contract():
    contract = {
        "id": "c1", "title": "TI", "value": 1000,
        "status": "active", "author_name": "Ana", "witness_name": "João", "deadline": "2025-12-01"
    }
    renderer = MCPRenderer()
    output = renderer.render_contract(contract)
    assert "Contrato #c1" in output
    assert "Ativo" in output or "🟢" in output