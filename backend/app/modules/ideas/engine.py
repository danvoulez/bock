from .mrl_parser import MRLParser, ASTNode

class IdeaExecutionEngine:
    def __init__(self, idea, context):
        self.idea = idea
        self.context = context  # Dict: {"idea": idea_obj, "user": user_obj, ...}
        self.parser = MRLParser()

    def execute_rule(self, rule_text):
        ast = self.parser.parse(rule_text)
        conditions = ast.children[0].value  # In production: AST traversal
        actions = ast.children[1].value

        if self._evaluate_conditions(conditions):
            for action in actions:
                self._execute_action(action)
            return True
        return False

    def _evaluate_conditions(self, cond_text):
        # TODO: Real parser for boolean logic
        # For now: support simple eval
        idea = self.context.get('idea')
        votes = getattr(idea, 'vote_count', 0)
        cost = getattr(idea, 'cost', 0)
        # Replace variables in cond_text
        cond_eval = cond_text.replace('idea.votos', str(votes)).replace('idea.custo', str(cost))
        cond_eval = cond_eval.replace('E', 'and').replace('OU', 'or')
        try:
            return eval(cond_eval)
        except Exception:
            return False

    def _execute_action(self, action):
        # Parse and execute supported actions
        if action.startswith('SETAR'):
            # SETAR campo = valor
            match = re.match(r'SETAR (\w+)\s*=\s*[\'"]?([\w\s]+)[\'"]?', action)
            if match:
                field, value = match.groups()
                setattr(self.idea, field, value)
        elif action.startswith('NOTIFICAR'):
            # NOTIFICAR destinatario MENSAGEM texto
            match = re.match(r'NOTIFICAR (\w+) MENSAGEM [\'"](.+)[\'"]', action)
            if match:
                destinatario, texto = match.groups()
                # Simulate notification (log or send)
                print(f"Notificando {destinatario}: {texto}")
        # TODO: Implementar CRIAR, DISPACHAR, EXECUTAR etc.

# Exemplo de uso:
# engine = IdeaExecutionEngine(idea_obj, context)
# engine.execute_rule("IDEIA PRIORIDADE-ALTA: (idea.votos >= 10) E (idea.custo <= 1000) -> SETAR status = 'aprovada', NOTIFICAR autor MENSAGEM 'Aprovada!'")