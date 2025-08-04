"""
app/modules/workflows/schemas.py

Schemas Pydantic para Workflows e Steps. Inclui modelos para criação, resposta e auditoria.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class WorkflowBase(BaseModel):
    name: str = Field(..., max_length=80)
    description: Optional[str]
    tenant_id: str

class WorkflowCreate(WorkflowBase):
    pass

class WorkflowResponse(WorkflowBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class WorkflowStepBase(BaseModel):
    workflow_id: UUID
    item_id: UUID
    item_type: str = Field(..., regex="^(idea|contract)$")
    step_order: int

class WorkflowStepCreate(WorkflowStepBase):
    pass

class WorkflowStepResponse(WorkflowStepBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True