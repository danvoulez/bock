import time
from app.modules.ideas.services import IdeaService

def test_priority_recalc_perf(monkeypatch):
    class DummyDB:
        async def execute(self, q): return [7,8,9,10]
        async def get(self, model, id): return type('Idea', (), {"initial_priority": 5, "priority_data": {"votes": [7,8,9,10]}})
        async def commit(self): pass

    db = DummyDB()
    start = time.time()
    # Simula recálculo de prioridade
    IdeaService.calculate_current_priority(db, db.get(None, None))
    elapsed = time.time() - start
    assert elapsed < 0.1  # Teste de performance simplificado