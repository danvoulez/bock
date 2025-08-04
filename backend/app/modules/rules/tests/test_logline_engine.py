import pytest
from app.modules.rules.logline_engine import LogLineEngine

@pytest.mark.asyncio
async def test_load_and_evaluate_rule():
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
            "votes": [7, 8, 9],
            "author": "Joana"
        }
    }
    # No momento, só checamos que não há erro no fluxo
    result = engine.evaluate("PRIORITY-IDEA", context)
    assert result is None  # Output é print, futuro: resultado do executor

def test_invalid_rule_syntax():
    engine = LogLineEngine()
    bad_rule_text = "RULE THIS_IS_INVALID No conditions or actions"
    with pytest.raises(ValueError):
        engine.load_rule(bad_rule_text)