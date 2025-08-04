from fastapi import FastAPI
from app.modules.rules.api import router as rules_router
# ... outros routers

app = FastAPI(title="Minicontratos API", version="0.2.0")

app.include_router(rules_router, prefix="/api", tags=["rules"])
# ... include outros routers

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Minicontratos API"}