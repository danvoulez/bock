"""
app/modules/workflows/service.py

Serviço Workflows: criação, execução, consulta de steps, integração com ideias/contratos.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Workflow, WorkflowStep
from .schemas import WorkflowCreate, WorkflowStepCreate
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class WorkflowService:
    @staticmethod
    async def create_workflow(db: AsyncSession, data: dict, tenant_id: str) -> Workflow:
        workflow = Workflow(
            tenant_id=tenant_id,
            **data,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(workflow)
        await db.commit()
        await db.refresh(workflow)
        return workflow

    @staticmethod
    async def list_workflows(db: AsyncSession, tenant_id: str) -> List[Workflow]:
        stmt = select(Workflow).where(Workflow.tenant_id == tenant_id)
        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def create_step(db: AsyncSession, data: dict) -> WorkflowStep:
        step = WorkflowStep(
            **data,
            created_at=datetime.utcnow()
        )
        db.add(step)
        await db.commit()
        await db.refresh(step)
        return step

    @staticmethod
    async def get_steps(db: AsyncSession, workflow_id: UUID) -> List[WorkflowStep]:
        stmt = select(WorkflowStep).where(WorkflowStep.workflow_id == workflow_id)
        result = await db.execute(stmt)
        return result.scalars().all()