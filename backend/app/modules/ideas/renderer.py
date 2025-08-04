class IdeaRenderer:
    @staticmethod
    def render_dashboard(ideas: list) -> str:
        rows = ["| ID | Título | Prioridade | Estado |\n|----|--------|------------|--------|"]
        for i in ideas:
            rows.append(f"| {i.id} | {i.title} | {i.priority_data['current']:.2f} | {i.workflow_state} |")
        return "\n".join(rows)

    @staticmethod
    def render_idea_card(idea: dict) -> str:
        return f"""
💡 **Ideia #{idea['id']}**
**Título**: {idea['title']}
**Prioridade Atual**: {idea['priority_data']['current']:.2f}
**Estado**: {idea['workflow_state']}
**Descrição**: {idea['description']}
[Votar] [Simular Impacto] [Detalhes]
"""