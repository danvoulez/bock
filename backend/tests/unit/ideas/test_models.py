import pytest
from app.modules.ideas.models import Idea

def test_idea_model_fields():
    idea = Idea(
        title="Teste",
        tenant_id="tenant_001",
        priority_data={"initial": 7, "current": 7, "votes": []},
        cost_data={"value": 150},
        workflow_state="DRAFT",
        author_id="author_001"
    )
    assert idea.title == "Teste"
    assert idea.tenant_id == "tenant_001"
    assert idea.priority_data["initial"] == 7
    assert idea.cost_data["value"] == 150
    assert idea.workflow_state == "DRAFT"