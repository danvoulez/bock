# Entry point do runtime do Minicontratos

from app.modules.rules.logline_engine import LogLineEngine
from app.modules.registry.models import Tenant, Person
from app.modules.contracts.models import Contract
from app.modules.ideas.models import Idea

class MinicontratosRuntime:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.engine = LogLineEngine()
        self.load_rules_for_tenant()

    def load_rules_for_tenant(self):
        # Carrega todos arquivos .lll do tenant
        rule_files = self._list_rule_files(self.tenant_id)
        for path in rule_files:
            with open(path) as f:
                self.engine.load_rule(f.read())

    def execute_rule(self, rule_id, context):
        # Executa regra pelo ID com contexto (ex: ideia, contrato, evento)
        return self.engine.evaluate(rule_id, context)

    def execute_workflow(self, workflow_id, context):
        # Orquestra execução de workflow via regras
        # Exemplo: sequencia de regras para aprovação de ideia > contrato > execução
        pass

    def audit(self, rule_id, context, result):
        # Log/audita execução da regra
        pass

    def _list_rule_files(self, tenant_id):
        # Retorna lista de arquivos .lll para o tenant
        import glob
        return glob.glob(f"rules/tenants/{tenant_id}/*.lll")