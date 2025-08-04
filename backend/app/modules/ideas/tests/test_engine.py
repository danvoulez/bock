from app.modules.ideas.engine import IdeaExecutionEngine

class DummyIdea:
    def __init__(self):
        self.vote_count = 12
        self.cost = 800
        self.status = 'pendente'

def test_engine_executes_set_and_notify(capsys):
    idea = DummyIdea()
    context = {"idea": idea, "autor": "João"}
    engine = IdeaExecutionEngine(idea, context)
    rule = "IDEIA PRIORIDADE-ALTA: (idea.votos >= 10) E (idea.custo <= 1000) -> SETAR status = 'aprovada', NOTIFICAR autor MENSAGEM 'Sua ideia foi aprovada!'"
    assert engine.execute_rule(rule)
    assert idea.status == 'aprovada'
    captured = capsys.readouterr()
    assert "Notificando autor" in captured.out