"""
app/utils/priority.py

Cálculo de prioridade de ideias. Utiliza regra ativa do tenant, fallback para média simples.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.modules.ideas.models import Idea, IdeaVote
from uuid import UUID

async def recalculate_priority(db: AsyncSession, idea_id: UUID):
    stmt = select(func.avg(IdeaVote.vote)).where(IdeaVote.idea_id == idea_id)
    result = await db.execute(stmt)
    avg_vote = result.scalar() or 0
    idea = await db.get(Idea, idea_id)
    if idea:
        initial = idea.initial_priority
        weights = idea.priority_data.get("weights") if idea.priority_data else None
        if weights:
            new_priority = (initial * weights.get("initial", 0.3)) + (avg_vote * weights.get("votes", 0.7))
        else:
            new_priority = (initial + avg_vote) / 2
        idea.current_priority = round(new_priority, 2)
        await db.commit()