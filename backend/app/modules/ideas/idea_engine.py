import uuid
from datetime import datetime
from app.modules.ideas.models import Idea
from app.modules.ideas.schemas import IdeaCreate, IdeaResponse, VoteCreate
from app.modules.ideas.voting_service import VotingService
from app.modules.ideas.simulator import IdeaSimulator
from app.core.tenant import get_current_tenant_id

class IdeaEngine:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.voting_service = VotingService(tenant_id)
        self.simulator = IdeaSimulator(tenant_id)

    async def create_idea(self, db, idea_data: dict, author):
        # Aplica contratos-regra da ideia
        idea_id = str(uuid.uuid4())
        now = datetime.utcnow()
        idea = Idea(
            id=idea_id,
            tenant_id=self.tenant_id,
            title=idea_data["title"],
            description=idea_data["description"],
            priority_data={
                "initial": idea_data.get("priority", 5.0),
                "current": idea_data.get("priority", 5.0),
                "votes": []
            },
            cost_data=idea_data.get("cost_data", {}),
            workflow_state="DRAFT",
            author_id=author.id,
            created_at=now,
            updated_at=now
        )
        db.add(idea)
        await db.commit()
        return idea

    async def vote_idea(self, db, idea_id, vote_data, voter):
        idea = await db.get(Idea, idea_id)
        updated_idea = await self.voting_service.cast_vote(db, idea, vote_data, voter)
        return updated_idea

    async def simulate_impact(self, db, idea_id, scenario="default"):
        idea = await db.get(Idea, idea_id)
        report = await self.simulator.run_simulation(db, idea, scenario)
        return report