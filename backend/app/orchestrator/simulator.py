class Simulator:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.rule_engine = RuleEngine(tenant_id, simulation=True)
        self.workflow_engine = WorkflowEngine(tenant_id, simulation=True)
        self.audit = AuditLogger(tenant_id, simulation=True)

    async def run_simulation(self, event_type, payload, user_context, scenario="default"):
        context = self._build_context(event_type, payload, user_context, scenario)
        self.audit.log_event(f"SIMULATION-{event_type}", context)

        # 1. Avalia regras e packs (simulado)
        rule_decisions = self.rule_engine.evaluate_all(event_type, context, simulated=True)

        # 2. Dispara workflows (simulado)
        wf_result = self.workflow_engine.maybe_trigger(event_type, context, rule_decisions, simulated=True)

        # 3. Gera relatório de consequências
        return self._simulate_report(rule_decisions, wf_result, context)

    def _build_context(self, event_type, payload, user_context, scenario):
        # Permite inserir dados fictícios, gerar cenários edge-case
        context = {
            **payload,
            "user": user_context,
            "tenant_id": self.tenant_id,
            "scenario": scenario
        }
        # Pode incluir manipulação de dados para stress-test
        return context

    def _simulate_report(self, rule_decisions, wf_result, context):
        # Retorna relatório detalhado: decisões, efeitos, riscos, logs
        return {
            "decisions": rule_decisions,
            "workflow": wf_result,
            "impact": self._estimate_impact(rule_decisions, wf_result),
            "log": self.audit.get_last_events()
        }

    def _estimate_impact(self, rule_decisions, wf_result):
        # Avalia consequências hipotéticas: penalidades, mudanças de estado, notificações
        pass