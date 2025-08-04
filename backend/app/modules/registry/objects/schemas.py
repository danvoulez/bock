"""
app/modules/registry/objects/schemas.py

Schemas Pydantic para Objetos do Registry. Inclui todos campos relevantes, validação, serialização, e integração com contratos.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID

class ObjectBase(BaseModel):
    name: str = Field(..., max_length=120)
    type: str = Field(..., max_length=50)
    tenant_id: str

class ObjectCreate(ObjectBase):
    pass

class ObjectResponse(ObjectBase):
    id: UUID
    alias: Optional[str]
    category: Optional[str]
    verified: bool
    owner_id: Optional[UUID]
    linked_to: Optional[UUID]
    rendering_uri: Optional[str]
    preview_text: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ObjectAuditLog(BaseModel):
    event: str
    timestamp: datetime
    actor_id: UUID
    details: dict