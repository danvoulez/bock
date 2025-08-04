import glob
import os
from app.modules.rules.logline_engine import LogLineEngine

class LogLineRuntime:
    def __init__(self, tenant_id="default"):
        self.tenant_id = tenant_id
        self.engine = LogLineEngine()
        self.rule_dir = f"app/modules/rules/tenants/{self.tenant_id}/"
        if not os.path.exists(self.rule_dir):
            self.rule_dir = "app/modules/rules/core/"
        self.load_rules()

    def load_rules(self):
        rule_files = glob.glob(os.path.join(self.rule_dir, "*.lll"))
        for path in rule_files:
            with open(path) as f:
                self.engine.load_rule(f.read())

    def evaluate(self, rule_id, context):
        return self.engine.evaluate(rule_id, context)

    def reload(self):
        self.engine = LogLineEngine()
        self.load_rules()