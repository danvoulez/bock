import pytest
from app.runtime.runtime import MinicontratosRuntime

@pytest.mark.asyncio
async def test_runtime_rule_evaluation():
    runtime = MinicontratosRuntime(tenant_id="default")
    context = {
        "idea": {
            "vote_count": 10,
            "initial_priority": 6,
            "votes": [8, 9, 10],
            "author": "Joana"
        }
    }
    # Assume que o arquivo 'core/priority.lll' existe e está correto
    result = runtime.execute_rule("PRIORITY-IDEA", context)
    assert result is None  # Output é print, futuro: resultado do executor

def test_runtime_reload_rules():
    runtime = MinicontratosRuntime(tenant_id="default")
    runtime.reload_rules()
    # Se não lançar erro, está ok