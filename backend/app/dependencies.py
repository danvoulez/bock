"""
app/dependencies.py

Dependências globais para FastAPI. Inclui banco, supabase, e contextos de tenant.
"""

from fastapi import Depends, Header
from app.core.database import get_db

def get_db_dependency():
    return Depends(get_db)

def get_tenant_id(x_tenant_id: str = Header(..., alias="X-Tenant-ID")):
    return x_tenant_id