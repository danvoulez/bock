import time
from app.modules.contracts.state_machine import ContractStateMachine, ContractState
from app.modules.contracts.models import Contract

def test_contract_state_machine_perf(monkeypatch):
    contract = Contract(id="c1", status=ContractState.ACTIVE.value)
    start = time.time()
    ContractStateMachine.can_transition(ContractState.ACTIVE, ContractState.QUESTIONED)
    elapsed = time.time() - start
    assert elapsed < 0.01