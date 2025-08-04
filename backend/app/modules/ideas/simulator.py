class IdeaSimulator:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id

    async def run_simulation(self, db, idea, scenario="default"):
        # Simula impacto da ideia: votos hipotéticos, mudanças de estado, workflow
        sim_votes = [10, 9, 8, 10, 7, 9]
        sim_priority = sum(sim_votes) / len(sim_votes)
        next_state = "APPROVED" if sim_priority >= 7 else "ARCHIVED"
        return {
            "idea_id": idea.id,
            "simulated_votes": sim_votes,
            "simulated_priority": sim_priority,
            "next_state": next_state,
            "message": f"Ideia atingiria estado '{next_state}' com prioridade simulada {sim_priority:.2f}"
        }