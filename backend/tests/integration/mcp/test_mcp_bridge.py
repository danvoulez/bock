import pytest
from mcp_bridge.protocol import MCPBridge

@pytest.mark.asyncio
async def test_mcp_admin_command():
    bridge = MCPBridge()
    response = await bridge.handle_request(
        {"id": "admin1", "role": "admin"},
        "UPDATE SYSTEM: Adicionar campo 'categoria' às ideias"
    )
    assert "system_update" in response["action"]
    assert "categoria" in response["parameters"]["fields"]

@pytest.mark.asyncio
async def test_mcp_user_command():
    bridge = MCPBridge()
    response = await bridge.handle_request(
        {"id": "user1", "role": "user"},
        "CREATE IDEA: Plataforma de backup automático com prioridade 8"
    )
    assert "create_idea" in response["action"]
    assert "backup automático" in response["parameters"]["title"]