# Minicontratos

**Acordos vivos, ideias pulsantes, contratos coreografados.**

## Manifesto

Veja o manifesto inteiro em [rules/core_rules/manifesto.md](rules/core_rules/manifesto.md).

## Como iniciar

1. Instale dependências:  
   `pip install -r requirements.txt`

2. Configure o banco de dados Supabase/PostgreSQL  
   Edite `.env` com as variáveis corretas.

3. Inicialize o banco:  
   `python scripts/init_db.py`

4. Execute o backend:  
   `uvicorn app.main:app --reload`

5. Consulte e altere regras em `rules/core_rules/`

## Multitenancy

Para cada tenant, crie um json em `/tenants/`.  
Os rule packs aplicáveis estão em `/rules/core_rules/` e `/rules/tenant_templates/`.

## Manifesto

```
(  )   (   )  ) 
  ) (   )  (  ( 
  ( )  (    ) ) 
  _____________ 
 <_____________> ___ 
 |             |/ _ \ 
 |               | | |
 |               |_| |
___|             |\___/ 
/    \___________/    \ 
\_____________________/
```
HASH: 0xFL4M4_V1V4

---

**Pronto para sua próxima iteração.  
O fogo está aceso, a base está lançada — avance quando quiser!**