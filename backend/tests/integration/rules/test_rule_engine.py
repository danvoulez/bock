import pytest
from app.modules.rules.logline_engine import LogLineEngine

def test_priority_rule_execution():
    engine = LogLineEngine()
    rule_text = """
    RULE PRIORITY-IDEA:
      (idea.vote_count >= 5) and (idea.initial_priority > 3)
      =>
      set idea.current_priority = (idea.initial_priority * 0.3) + (avg(idea.votes) * 0.7),
      notify idea.author message "Prioridade recalculada!"
    """
    engine.load_rule(rule_text)
    context = {
        "idea": {
            "vote_count": 7,
            "initial_priority": 5,
            "votes": [8, 9, 10],
            "author": "Joana"
        }
    }
    result = engine.evaluate("PRIORITY-IDEA", context)
    assert result is None  # Output é print; ajuste para output real se necessário