"""
app/modules/workflows/api.py

Endpoints FastAPI para Workflows e Steps. Suporte a multitenancy e auditoria.
"""

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from app.core.database import get_db
from .service import WorkflowService
from .schemas import WorkflowCreate, WorkflowResponse, WorkflowStepCreate, WorkflowStepResponse

router = APIRouter()

@router.post("/", response_model=WorkflowResponse, status_code=status.HTTP_201_CREATED)
async def create_workflow(
    workflow: WorkflowCreate,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    new_workflow = await WorkflowService.create_workflow(db, workflow.dict(), tenant_id)
    return new_workflow

@router.get("/", response_model=List[WorkflowResponse])
async def list_workflows(
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    return await WorkflowService.list_workflows(db, tenant_id)

@router.post("/steps", response_model=WorkflowStepResponse, status_code=status.HTTP_201_CREATED)
async def create_step(
    step: WorkflowStepCreate,
    db: AsyncSession = Depends(get_db)
):
    new_step = await WorkflowService.create_step(db, step.dict())
    return new_step

@router.get("/{workflow_id}/steps", response_model=List[WorkflowStepResponse])
async def get_steps(
    workflow_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await WorkflowService.get_steps(db, workflow_id)