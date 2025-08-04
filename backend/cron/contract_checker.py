"""
cron/contract_checker.py

Verificação de contratos em estado questionado, dispara penalidades automáticas e despachos conforme regras.
Auditoria rigorosa e integração com enforcement/dispatch.
"""

import asyncio
from datetime import datetime, timedelta
from app.core.database import AsyncSessionLocal
from app.modules.contracts.models import Contract
from app.modules.contracts.service import ContractService
from app.armor.audit_logger import log_system_action
from sqlalchemy import select

async def check_pending_penalties():
    async with AsyncSessionLocal() as db:
        # Contratos em estado QUESTIONADO há mais de 15 dias
        threshold = datetime.utcnow() - timedelta(days=15)
        contracts = await db.execute(
            select(Contract)
            .where(Contract.status == "QUESTIONADO")
            .where(Contract.updated_at < threshold)
        )
        for contract in contracts.scalars().all():
            try:
                await ContractService.apply_penalty(
                    db, contract.id, amount=contract.value * 0.1,
                    reason="Penalidade automática por questionamento não resolvido"
                )
                log_system_action("CONTRACT_PENALTY", f"Contrato {contract.id} penalizado automaticamente.")
            except Exception as e:
                log_system_action("CONTRACT_PENALTY_ERROR", str(e), level="ERROR")

if __name__ == "__main__":
    asyncio.run(check_pending_penalties())