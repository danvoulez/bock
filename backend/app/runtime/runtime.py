import glob
import os
from app.modules.rules.logline_engine import LogLineEngine

class MinicontratosRuntime:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.engine = LogLineEngine()
        self.load_rules_for_tenant()

    def load_rules_for_tenant(self):
        rule_dir = f"app/modules/rules/tenants/{self.tenant_id}/"
        if not os.path.exists(rule_dir):
            rule_dir = "app/modules/rules/core/"
        rule_files = glob.glob(os.path.join(rule_dir, "*.lll"))
        for path in rule_files:
            with open(path) as f:
                self.engine.load_rule(f.read())

    def execute_rule(self, rule_id, context):
        result = self.engine.evaluate(rule_id, context)
        self.audit(rule_id, context, result)
        return result

    def audit(self, rule_id, context, result):
        print(f"[AUDIT] rule: {rule_id}, context: {context}, result: {result}")

    def reload_rules(self):
        self.engine = LogLineEngine()
        self.load_rules_for_tenant()