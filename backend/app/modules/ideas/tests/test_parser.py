import pytest
from app.modules.ideas.mrl_parser import MRLParser

def test_parser_basic():
    parser = MRLParser()
    rule = "IDEIA TESTE: (idea.votos >= 5) E (idea.custo < 2000) -> SETAR status = 'valida', NOTIFICAR autor MENSAGEM 'Validação OK'"
    ast = parser.parse(rule)
    assert ast.nodetype == 'rule'
    assert ast.children[0].nodetype == 'conditions'
    assert 'idea.votos' in ast.children[0].value
    assert 'SETAR status' in ast.children[1].value[0]

def test_parser_error():
    parser = MRLParser()
    with pytest.raises(Exception):
        parser.parse("IDEIA SEM SETA (faltando '->')")