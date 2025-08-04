"""
app/modules/contracts/api.py

Endpoints FastAPI para contratos.
Inclui criação, listagem, despacho, penalidades, workflow de estados, auditoria e integração com multitenancy e contratos-regra.
"""

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from app.core.database import get_db
from .service import ContractService
from .schemas import (
    ContractCreate, ContractResponse, DispatchCreate, DispatchResponse,
    PenaltyCreate, PenaltyResponse
)

router = APIRouter()

@router.post("/", response_model=ContractResponse, status_code=status.HTTP_201_CREATED)
async def create_contract(
    contract: ContractCreate,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    obj = await ContractService.create_contract(db, contract.dict(), tenant_id)
    return obj

@router.get("/", response_model=List[ContractResponse])
async def list_contracts(
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    status: str = None,
    db: AsyncSession = Depends(get_db)
):
    return await ContractService.list_contracts(db, tenant_id, status)

@router.get("/{contract_id}", response_model=ContractResponse)
async def get_contract(
    contract_id: UUID,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    obj = await ContractService.get_contract(db, contract_id, tenant_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return obj

@router.post("/{contract_id}/dispatch", response_model=DispatchResponse, status_code=status.HTTP_201_CREATED)
async def create_dispatch(
    contract_id: UUID,
    payload: DispatchCreate,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    contract = await ContractService.get_contract(db, contract_id, tenant_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    dispatch = await ContractService.create_dispatch(db, contract_id, payload.dispatched_to, payload.reason)
    return dispatch

@router.post("/dispatch/{dispatch_id}/accept", response_model=DispatchResponse)
async def accept_dispatch(
    dispatch_id: UUID,
    member_id: UUID,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    dispatch = await ContractService.accept_dispatch(db, dispatch_id, member_id)
    if not dispatch:
        raise HTTPException(status_code=404, detail="Despacho não encontrado")
    return dispatch

@router.post("/{contract_id}/penalty", response_model=PenaltyResponse, status_code=status.HTTP_201_CREATED)
async def apply_penalty(
    contract_id: UUID,
    payload: PenaltyCreate,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    contract = await ContractService.get_contract(db, contract_id, tenant_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    penalty = await ContractService.apply_penalty(db, contract_id, payload.amount, payload.reason or "Penalidade automática")
    return penalty

@router.get("/{contract_id}/audit", response_model=List[dict])
async def audit_log(
    contract_id: UUID,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_db)
):
    contract = await ContractService.get_contract(db, contract_id, tenant_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return await ContractService.audit_log(db, contract_id)