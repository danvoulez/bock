"""
app/modules/contracts/service.py

Serviço principal para contratos.
Implementa lógica de negócio: submissão, despacho, acionamento, penalidades, workflow de estados e integração com contratos-regra.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func
from .models import Contract, Dispatch, Penalty
from .schemas import (
    ContractCreate, ContractResponse, DispatchCreate, DispatchResponse,
    PenaltyCreate, PenaltyResponse
)
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class ContractService:
    @staticmethod
    async def create_contract(db: AsyncSession, data: dict, tenant_id: str) -> Contract:
        contract = Contract(
            tenant_id=tenant_id,
            **data,
            status="ATIVO",
            workflow_state="ATIVO",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(contract)
        await db.commit()
        await db.refresh(contract)
        return contract

    @staticmethod
    async def list_contracts(db: AsyncSession, tenant_id: str, status: Optional[str] = None) -> List[Contract]:
        query = select(Contract).where(Contract.tenant_id == tenant_id)
        if status:
            query = query.where(Contract.status == status)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_contract(db: AsyncSession, contract_id: UUID, tenant_id: str) -> Optional[Contract]:
        stmt = select(Contract).where(Contract.id == contract_id, Contract.tenant_id == tenant_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def create_dispatch(db: AsyncSession, contract_id: UUID, dispatched_to: UUID, reason: str) -> Dispatch:
        dispatch = Dispatch(
            contract_id=contract_id,
            dispatched_to=dispatched_to,
            reason=reason,
            status="pending",
            created_at=datetime.utcnow(),
            logline={
                "event": "DISPATCH",
                "timestamp": datetime.utcnow().isoformat(),
                "actor_id": str(dispatched_to),
                "details": {"reason": reason}
            }
        )
        db.add(dispatch)
        await db.commit()
        await db.refresh(dispatch)
        await ContractService.update_contract_state(db, contract_id, "DESPACHADO")
        return dispatch

    @staticmethod
    async def accept_dispatch(db: AsyncSession, dispatch_id: UUID, member_id: UUID) -> Dispatch:
        dispatch = await db.get(Dispatch, dispatch_id)
        if not dispatch:
            return None
        dispatch.status = "accepted"
        dispatch.dispatched_to = member_id
        dispatch.logline = {
            "event": "DISPATCH_ACCEPTED",
            "timestamp": datetime.utcnow().isoformat(),
            "actor_id": str(member_id),
            "details": {"dispatch_id": str(dispatch_id)}
        }
        await db.commit()
        contract = await db.get(Contract, dispatch.contract_id)
        if contract:
            contract.witness_id = member_id
            await ContractService.update_contract_state(db, contract.id, "ATIVO")
        return dispatch

    @staticmethod
    async def apply_penalty(db: AsyncSession, contract_id: UUID, amount: float, reason: str) -> Penalty:
        penalty = Penalty(
            contract_id=contract_id,
            amount=amount,
            reason=reason,
            applied_at=datetime.utcnow(),
            logline={
                "event": "PENALTY",
                "timestamp": datetime.utcnow().isoformat(),
                "details": {"amount": amount, "reason": reason}
            }
        )
        db.add(penalty)
        await db.commit()
        await db.refresh(penalty)
        await ContractService.update_contract_state(db, contract_id, "PENALIZADO")
        return penalty

    @staticmethod
    async def update_contract_state(db: AsyncSession, contract_id: UUID, new_state: str):
        stmt = update(Contract).where(Contract.id == contract_id).values(
            status=new_state,
            workflow_state=new_state,
            updated_at=datetime.utcnow()
        )
        await db.execute(stmt)
        await db.commit()

    @staticmethod
    async def audit_log(db: AsyncSession, contract_id: UUID) -> List[dict]:
        dispatches = await db.execute(select(Dispatch).where(Dispatch.contract_id == contract_id))
        penalties = await db.execute(select(Penalty).where(Penalty.contract_id == contract_id))
        logs = []
        logs.extend([d.logline for d in dispatches.scalars() if d.logline])
        logs.extend([p.logline for p in penalties.scalars() if p.logline])
        return logs

    # Acionamento automático de penalidades e despacho pode ser implementado via cron/worker