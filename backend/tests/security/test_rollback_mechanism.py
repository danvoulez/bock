from app.armor.auto_rollback import AutoRollbackSystem

def test_db_rollback(monkeypatch):
    called = {}
    def fake_downgrade(cfg, version): called['rollback'] = True
    monkeypatch.setattr("alembic.command.downgrade", fake_downgrade)
    AutoRollbackSystem.db_rollback("prev")
    assert called.get('rollback')

def test_code_rollback(monkeypatch):
    called = {}
    def fake_run(args, check): called['code'] = True
    monkeypatch.setattr("subprocess.run", fake_run)
    AutoRollbackSystem.code_rollback("HEAD@{1}")
    assert called.get('code')