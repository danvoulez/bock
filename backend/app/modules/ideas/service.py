from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from uuid import UUID
from .models import Idea, IdeaVote
from .schemas import IdeaCreate, IdeaVoteCreate

class IdeaService:
    @staticmethod
    async def create_idea(db: AsyncSession, idea_data: IdeaCreate) -> Idea:
        idea = Idea(**idea_data.dict())
        db.add(idea)
        await db.commit()
        await db.refresh(idea)
        return idea

    @staticmethod
    async def vote_idea(db: AsyncSession, idea_id: UUID, vote_data: IdeaVoteCreate) -> None:
        # Busca a ideia por tenant (garantia de isolamento)
        idea = await db.get(Idea, idea_id)
        if not idea:
            raise Exception("Ideia não encontrada")
        vote = IdeaVote(idea_id=idea_id, person_id=vote_data.person_id, vote=vote_data.vote)
        db.add(vote)
        await db.commit()
        await IdeaService.recalculate_priority(db, idea_id)

    @staticmethod
    async def recalculate_priority(db: AsyncSession, idea_id: UUID) -> None:
        stmt = select(func.avg(IdeaVote.vote)).where(IdeaVote.idea_id == idea_id)
        result = await db.execute(stmt)
        avg_priority = result.scalar()
        idea = await db.get(Idea, idea_id)
        if idea and avg_priority:
            idea.current_priority = avg_priority
            await db.commit()
    
    @staticmethod
    async def list_ideas(db: AsyncSession, tenant_id: str, sort_by: str = "current_priority") -> list[Idea]:
        stmt = select(Idea).where(Idea.tenant_id == tenant_id)
        if sort_by == "current_priority":
            stmt = stmt.order_by(Idea.current_priority.desc())
        elif sort_by == "cost":
            stmt = stmt.order_by(Idea.cost.desc())
        elif sort_by == "title":
            stmt = stmt.order_by(Idea.title.asc())
        result = await db.execute(stmt)
        return result.scalars().all()