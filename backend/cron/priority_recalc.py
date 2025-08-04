"""
cron/priority_recalc.py

Rotina periódica de recálculo de prioridades das ideias.
Executa motor de regras para todas ideias ativas e audita alterações.
"""

import asyncio
from app.core.database import AsyncSessionLocal
from app.modules.ideas.models import Idea
from app.utils.priority import recalculate_priority
from sqlalchemy import select
from app.armor.audit_logger import log_system_action

async def recalc_all_priorities():
    async with AsyncSessionLocal() as db:
        ideas = await db.execute(select(Idea).where(Idea.workflow_state != "ARQUIVADO"))
        for idea in ideas.scalars().all():
            try:
                await recalculate_priority(db, idea.id)
                log_system_action("PRIORITY_RECALC", f"Ideia {idea.id} prioridade recalculada.")
            except Exception as e:
                log_system_action("PRIORITY_RECALC_ERROR", str(e), level="ERROR")

if __name__ == "__main__":
    asyncio.run(recalc_all_priorities())