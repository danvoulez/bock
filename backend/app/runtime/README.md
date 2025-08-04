# Runtime LogLine Lang (.lll) - Minicontratos

Este módulo implementa o runtime do motor LogLine (.lll), capaz de carregar, executar, auditar e versionar regras por tenant em tempo real.

## Componentes

- **runtime.py**: Classe principal que gerencia regras .lll por tenant, executa e audita.
- **api.py**: Endpoints FastAPI para executar regras e recarregar runtime.
- **tests/test_runtime.py**: Testes automáticos do runtime.

## Como funciona

1. **Carregamento de regras**: Busca arquivos .lll pelo tenant.
2. **Execução**: Executa regra pelo ID, com contexto (ideia, contrato, workflow).
3. **Auditoria**: Registra toda execução para rastreabilidade.
4. **Hot-reload**: Atualiza regras sem reiniciar backend.

## Exemplo de uso

```python
runtime = MinicontratosRuntime(tenant_id="tenant_001")
context = {"idea": {...}, "user": {...}}
result = runtime.execute_rule("PRIORITY-IDEA", context)
```

## API

- `POST /runtime/execute/{rule_id}`: Executa regra para o tenant.
- `POST /runtime/reload`: Recarrega regras .lll do tenant.

## Testes

```bash
pytest app/runtime/tests/
```