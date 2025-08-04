"""
app/modules/contracts/schemas.py

Schemas Pydantic para contratos, despachos, penalidades, workflows e auditoria.
Inclui modelos para criação, resposta, workflow de estados e integração com regras.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID

class ContractBase(BaseModel):
    title: str = Field(..., max_length=120)
    description: Optional[str] = Field(None, max_length=2000)
    value: float = Field(..., ge=0)
    deadline: Optional[datetime]
    penalty: Optional[str]
    normal_consequence: Optional[str]
    questioning_procedure: Optional[str]
    penalty_procedure: Optional[str]
    workflow_state: Optional[str] = "ATIVO"
    rule_definition: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ContractCreate(ContractBase):
    author_id: UUID
    witness_id: UUID
    tenant_id: str

class ContractResponse(ContractBase):
    id: UUID
    tenant_id: str
    status: str
    triggered_at: Optional[datetime]
    dispatched_to: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class DispatchBase(BaseModel):
    reason: str
    dispatched_to: Optional[UUID]

class DispatchCreate(DispatchBase):
    contract_id: UUID

class DispatchResponse(DispatchBase):
    id: UUID
    contract_id: UUID
    status: str
    created_at: datetime
    logline: Optional[dict]

    class Config:
        orm_mode = True

class PenaltyBase(BaseModel):
    amount: float = Field(..., ge=0)
    reason: Optional[str]

class PenaltyCreate(PenaltyBase):
    contract_id: UUID

class PenaltyResponse(PenaltyBase):
    id: UUID
    contract_id: UUID
    applied_at: datetime
    logline: Optional[dict]

    class Config:
        orm_mode = True

class ContractAuditLog(BaseModel):
    event: str
    timestamp: datetime
    actor_id: UUID
    details: dict