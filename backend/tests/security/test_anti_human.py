from app.armor.anti_human import HumanErrorProtection

def test_dangerous_command_blocking():
    assert not HumanErrorProtection.validate_destructive_command("DROP TABLE ideas")
    assert not HumanErrorProtection.validate_destructive_command("DELETE FROM contracts")
    assert HumanErrorProtection.validate_destructive_command("SELECT * FROM ideas")

def test_confirmation_escalation():
    assert not HumanErrorProtection.confirm_high_impact_action("user", "DROP DATABASE")