from app.modules.rules.logline_parser import LogLineParser

def test_parse_valid_rule():
    rule_text = """
    RULE PRIORITY-IDEA:
      (idea.vote_count >= 5) and (idea.initial_priority > 3)
      =>
      set idea.current_priority = (idea.initial_priority * 0.3) + (avg(idea.votes) * 0.7),
      notify idea.author message "Prioridade recalculada!"
    """
    parser = LogLineParser()
    rule = parser.parse(rule_text)
    assert rule.rule_id == "PRIORITY-IDEA"
    assert "idea.vote_count" in rule.conditions
    assert "set idea.current_priority" in rule.actions[0]

def test_parse_invalid_rule():
    parser = LogLineParser()
    with pytest.raises(ValueError):
        parser.parse("RULE falta tudo")