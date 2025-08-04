from .logline_parser import LogLineParser
from typing import Dict, Any, Callable

class LogLineEngine:
    def __init__(self):
        self.rules: Dict[str, Callable] = {}

    def load_rule(self, rule_text: str):
        parser = LogLineParser()
        rule = parser.parse(rule_text)
        exec_fn = self.compile_rule(rule)
        self.rules[rule.rule_id] = exec_fn

    def compile_rule(self, rule) -> Callable:
        # Placeholder: compile conditions/actions into Python function
        def exec_fn(context: Dict[str, Any]):
            print(f"Evaluating rule {rule.rule_id} with context {context}")
            print(f"Conditions: {rule.conditions}")
            print(f"Actions: {rule.actions}")
        return exec_fn

    def evaluate(self, rule_id: str, context: Dict[str, Any]):
        if rule_id not in self.rules:
            raise ValueError("Rule not loaded")
        return self.rules[rule_id](context)