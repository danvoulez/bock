import re

class Rule:
    def __init__(self, rule_id, conditions, actions):
        self.rule_id = rule_id
        self.conditions = conditions
        self.actions = actions

class RuleParser:
    RULE_REGEX = r'RULE (\w+):\s*(.+?)\s*->\s*(.+)'
    
    def parse(self, text):
        match = re.match(self.RULE_REGEX, text, re.DOTALL)
        if not match:
            raise ValueError("Invalid rule syntax")
        rule_id, conds, acts = match.groups()
        conditions = self._parse_conditions(conds)
        actions = self._parse_actions(acts)
        return Rule(rule_id, conditions, actions)
    
    def _parse_conditions(self, conds):
        # Placeholder: implement recursive parsing for AND/OR/NOT, etc.
        conds = conds.strip()
        return conds
    
    def _parse_actions(self, acts):
        # Placeholder: parse actions into AST nodes
        return [a.strip() for a in acts.split(',')]