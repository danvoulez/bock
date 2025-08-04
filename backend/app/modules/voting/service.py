"""
app/modules/voting/service.py

Serviço de votação compartilhado para ideias. Lógica de casting, update, e integração com prioridade.
"""

from app.utils.priority import recalculate_priority
from app.modules.ideas.models import IdeaVote, Idea
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from datetime import datetime

class VotingService:
    @staticmethod
    async def cast_vote(db: AsyncSession, idea_id: UUID, person_id: UUID, score: int) -> IdeaVote:
        stmt = select(IdeaVote).where(IdeaVote.idea_id == idea_id, IdeaVote.person_id == person_id)
        result = await db.execute(stmt)
        existing_vote = result.scalar_one_or_none()

        if existing_vote:
            existing_vote.vote = score
            existing_vote.created_at = datetime.utcnow()
        else:
            vote = IdeaVote(
                idea_id=idea_id,
                person_id=person_id,
                vote=score,
                created_at=datetime.utcnow()
            )
            db.add(vote)
        await db.commit()
        await recalculate_priority(db, idea_id)
        return existing_vote if existing_vote else vote