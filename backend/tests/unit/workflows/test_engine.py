from app.modules.workflows.engine import WorkflowEngine
from unittest.mock import AsyncMock

def test_execute_workflow_steps(monkeypatch):
    db = AsyncMock()
    workflow_id = "wf_001"
    monkeypatch.setattr("app.modules.workflows.engine.WorkflowService.get_steps", lambda db, wid: [type('Step', (), {"entity_type": "idea", "entity_id": "id1", "step_order": 1})])
    result = WorkflowEngine.execute_workflow(db, workflow_id)
    assert result