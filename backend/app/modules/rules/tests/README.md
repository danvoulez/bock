# Testes Automatizados do Motor de Regras LogLine (.lll)

## Objetivo

Testar o carregamento, parsing e execução de regras LogLine Lang (.lll), garantir integração com runtime modular e preparar base para integração MCP/API.

## Testes incluídos

- **test_logline_engine.py**:  
  - Carregamento de regra válida  
  - Execução com contexto real  
  - Detecção de sintaxe inválida

- **test_runtime.py**:  
  - Execução de regra via runtime multitenant  
  - Reload dinâmico de regras por tenant

## Como rodar

```bash
pytest app/modules/rules/tests/
pytest app/runtime/tests/
```

## Próximos testes

- Testes de auditoria e logging
- Testes de segurança e sandbox
- Testes de integração MCP/API
- Testes de performance e escalabilidade

## Observações

- Por enquanto, o executor só faz print; futuro: retorna resultado da ação.
- Testes são assíncronos, compatíveis com FastAPI/SQLAlchemy.