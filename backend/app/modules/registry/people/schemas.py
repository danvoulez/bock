"""
app/modules/registry/people/schemas.py

Schemas Pydantic para Pessoas do Registry. Inclui todos campos relevantes, validação, e serialização.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID

class PersonBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: Optional[EmailStr]
    phone: Optional[str]
    role: Optional[str]

class PersonCreate(PersonBase):
    tenant_id: str

class PersonResponse(PersonBase):
    id: UUID
    tenant_id: str
    ghost: bool
    verified: bool
    reputation: Optional[float]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PersonAuditLog(BaseModel):
    event: str
    timestamp: datetime
    actor_id: UUID
    details: dict