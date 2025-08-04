import re

class MRLParseError(Exception):
    pass

class ASTNode:
    def __init__(self, nodetype, value=None, children=None):
        self.nodetype = nodetype
        self.value = value
        self.children = children or []

class MRLParser:
    def __init__(self, grammar=None):
        # Grammar could be used for validation or hints
        pass

    def parse(self, rule_text):
        # Simplified parser: splits condition and actions
        try:
            if ':' not in rule_text or '->' not in rule_text:
                raise MRLParseError("Regra deve conter ':' e '->'")
            head, rest = rule_text.split(':', 1)
            cond_text, act_text = rest.split('->', 1)
            cond_ast = self._parse_conditions(cond_text.strip())
            act_ast = self._parse_actions(act_text.strip())
            return ASTNode('rule', head.strip(), [cond_ast, act_ast])
        except Exception as e:
            raise MRLParseError(f"Erro ao parsear regra: {str(e)}")

    def _parse_conditions(self, cond_text):
        # Placeholder: parse basic boolean expressions
        # TODO: Expand for full grammar
        return ASTNode('conditions', cond_text)

    def _parse_actions(self, act_text):
        # Split actions by ','
        actions = [a.strip() for a in act_text.split(',')]
        return ASTNode('actions', actions)

# Example of usage:
# parser = MRLParser()
# ast = parser.parse("IDEIA PRIORIDADE-ALTA: (idea.votos >= 10) E (idea.custo <= 1000) -> SETAR idea.status = 'aprovada', NOTIFICAR autor MENSAGEM 'Ideia aprovada!'")