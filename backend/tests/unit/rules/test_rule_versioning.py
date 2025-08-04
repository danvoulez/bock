from app.modules.rules.rule_versioning import RuleVersionControl

def test_commit_rule(monkeypatch):
    called = {}
    class FakeSB:
        def table(self, name): return self
        def insert(self, rule): called['commit'] = rule; return self
        def execute(self): return True
    rvc = RuleVersionControl("tenant_007")
    rvc.sb = FakeSB()
    rvc.commit_rule({"type": "validation"}, author=type("User", (), {"id": "u1"}), message="Novo commit")
    assert called.get('commit')

def test_get_rule_history(monkeypatch):
    class FakeSB:
        def table(self, name): return self
        def select(self, x): return self
        def eq(self, k, v): return self
        def order(self, k, desc): return self
        def execute(self): return [{"version": "v1"}]
    rvc = RuleVersionControl("tenant_007")
    rvc.sb = FakeSB()
    history = rvc.get_rule_history("rule_123")
    assert isinstance(history, list)