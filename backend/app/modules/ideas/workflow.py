class IdeaWorkflow:
    def __init__(self, idea, workflow_steps):
        self.idea = idea
        self.workflow_steps = workflow_steps  # List of (condition, action_rule) tuples

    def run(self, context):
        for condition, rule_text in self.workflow_steps:
            engine = IdeaExecutionEngine(self.idea, context)
            if engine._evaluate_conditions(condition):
                engine.execute_rule(rule_text)