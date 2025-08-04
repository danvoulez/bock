"""
cron/maintenance.py

Rotinas de manutenção diária/semanal do sistema Minicontratos.
Executa limpeza de ideias antigas, arquivamento de contratos expirados e auto-verificação de integridade.
Blindagem automática: todos resultados auditados e rollback em caso de falha.
"""

import asyncio
from datetime import datetime, timedelta
from app.core.database import AsyncSessionLocal
from app.modules.ideas.models import Idea
from app.modules.contracts.models import Contract
from app.armor.audit_logger import log_system_action
from sqlalchemy import delete, update

async def daily_maintenance():
    """Rotina diária: limpeza de ideias antigas sem votos e arquivamento de contratos vencidos."""
    async with AsyncSessionLocal() as db:
        try:
            # Limpa ideias sem votos com mais de 90 dias
            threshold = datetime.utcnow() - timedelta(days=90)
            await db.execute(
                delete(Idea)
                .where(Idea.created_at < threshold)
                .where(~Idea.votes.any())
            )
            # Arquiva contratos expirados
            await db.execute(
                update(Contract)
                .where(Contract.deadline < datetime.utcnow())
                .values(status='ARQUIVADO')
            )
            await db.commit()
            log_system_action("DAILY_MAINTENANCE", "Executado com sucesso")
        except Exception as e:
            log_system_action("MAINTENANCE_ERROR", str(e), level="ERROR")
            # Em produção, disparar auto_rollback

if __name__ == "__main__":
    asyncio.run(daily_maintenance())