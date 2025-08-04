# LogLine Lang - Motor de Regras Minicontratos

Este módulo implementa o engine nativo da linguagem **LogLine (.lll)** para o sistema Minicontratos.

## O que é LogLine?

LogLine é uma linguagem declarativa para expressar regras de contratos vivos, workflows, despacho, acionamentos e governança.
Permite que cada tenant, admin ou comunidade escreva suas próprias regras, com sintaxe legível e poder expressivo.

## Arquivos e Gramática

- **.lll**: Arquivos de regra (ex: core/priority.lll)
- **logline_grammar.py**: Gramática formal BNF
- **logline_parser.py**: Parser sintático para regras LogLine
- **logline_engine.py**: Executor e compilador de regras

## Exemplo de regra LogLine (.lll)

```lll
RULE PRIORITY-IDEA:
  (idea.vote_count >= 5) and (idea.initial_priority > 3)
  =>
  set idea.current_priority = (idea.initial_priority * 0.3) + (avg(idea.votes) * 0.7),
  notify idea.author message "Prioridade recalculada!"
```

## Como usar

```python
from app.modules.rules.logline_engine import LogLineEngine

engine = LogLineEngine()
with open("core/priority.lll") as f:
    engine.load_rule(f.read())
context = {
    "idea": {"vote_count": 7, "initial_priority": 5, "votes": [7,8,9], "author": "Joana"},
    "contract": {"state": "questioned", "question_timeout": 16, "parties": ["A", "B"], "author": "Joana"}
}
engine.evaluate("PRIORITY-IDEA", context)
```

## Eficiência

- Parsing busca apenas arquivos `.lll`
- Hot-reload: Mudou .lll, recompila só aquele AST
- AST caching: Cada .lll vira AST em memória ou banco
- Tenant isolation: Cada tenant pode ter seu pacote de regras .lll

## Extensões

- Plugável no MCP/ChatGPT e API REST
- Suporte a versionamento e auditoria de regras
- Cada tenant pode ter seus próprios pacotes .lll

## Segurança

- TODO: Implementar sandbox rigorosa para proteção
- TODO: AST e validação semântica

## Veja também

- [Manifesto Minicontratos](../manifesto.md)
- [Pacotes de Sugestão](../suggestion_packs/)