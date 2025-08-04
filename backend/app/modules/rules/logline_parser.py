import re
from typing import Any, Dict, List

class LogLineRule:
    def __init__(self, rule_id, conditions, actions):
        self.rule_id = rule_id
        self.conditions = conditions
        self.actions = actions

class LogLineParser:
    RULE_REGEX = r'RULE (\w+):\s*(.+?)\s*=>\s*(.+)'

    def parse(self, text: str) -> LogLineRule:
        match = re.match(self.RULE_REGEX, text, re.DOTALL | re.IGNORECASE)
        if not match:
            raise ValueError("Invalid LogLine syntax")
        rule_id, conds, acts = match.groups()
        conditions = conds.strip()
        actions = [a.strip() for a in acts.split(',')]
        return LogLineRule(rule_id, conditions, actions)