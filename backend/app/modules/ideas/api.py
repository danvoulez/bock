from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.modules.ideas.idea_engine import IdeaEngine
from app.modules.registry.service import RegistryService

router = APIRouter()

@router.post("/ideas", response_model=IdeaResponse)
async def create_idea(idea: IdeaCreate, x_tenant_id: str = Header(...), db: AsyncSession = Depends(get_db)):
    tenant_id = x_tenant_id
    engine = IdeaEngine(tenant_id)
    author = await RegistryService.get_person(idea.author_id, tenant_id)
    result = await engine.create_idea(db, idea.dict(), author)
    return result

@router.post("/ideas/{idea_id}/vote")
async def vote_idea(idea_id: str, vote: VoteCreate, x_tenant_id: str = Header(...), db: AsyncSession = Depends(get_db)):
    tenant_id = x_tenant_id
    engine = IdeaEngine(tenant_id)
    voter = await RegistryService.get_person(vote.voter_id, tenant_id)
    result = await engine.vote_idea(db, idea_id, vote.dict(), voter)
    return {"message": "Voto registrado", "priority": result.priority_data["current"]}

@router.post("/ideas/{idea_id}/simulate")
async def simulate_impact(idea_id: str, x_tenant_id: str = Header(...), db: AsyncSession = Depends(get_db)):
    tenant_id = x_tenant_id
    engine = IdeaEngine(tenant_id)
    sim_report = await engine.simulate_impact(db, idea_id)
    return {"result": sim_report}