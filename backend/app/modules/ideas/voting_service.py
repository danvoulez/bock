from app.modules.ideas.models import Idea, IdeaVote
from app.modules.rules.rule_engine import RuleEngine
from datetime import datetime

class VotingService:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.rule_engine = RuleEngine(tenant_id)

    async def cast_vote(self, db, idea, vote_data, voter):
        # Verifica regra de voto do tenant
        rule = self.rule_engine.get_rule("IDEA-VOTING-SIMPLE")
        max_votes = rule.get("restricoes", {}).get("votos_por_usuario", 1)

        # Checa se usuário já votou
        existing_votes = [v for v in idea.priority_data["votes"] if v["voter_id"] == voter.id]
        if len(existing_votes) >= max_votes:
            raise Exception("Voto já registrado")

        # Registra o voto
        vote = {
            "voter_id": voter.id,
            "score": vote_data["score"],
            "voted_at": datetime.utcnow()
        }
        idea.priority_data["votes"].append(vote)

        # Recalcula prioridade via regra do tenant
        scores = [v["score"] for v in idea.priority_data["votes"]]
        formula = rule.get("formula", "prioridade_atual = MEDIA(votos)")
        if formula == "prioridade_atual = MEDIA(votos)":
            idea.priority_data["current"] = sum(scores) / len(scores) if scores else idea.priority_data["initial"]
        # Extensível para outras fórmulas

        db.add(idea)
        await db.commit()
        return idea