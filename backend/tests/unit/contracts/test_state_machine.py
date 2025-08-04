import pytest
from app.modules.contracts.models import Contract
from app.modules.contracts.state_machine import ContractStateMachine, ContractState

@pytest.mark.asyncio
async def test_contract_state_transitions(db_session):
    contract = Contract(
        id="c1",
        status=ContractState.ACTIVE.value
    )
    db_session.add(contract)
    await db_session.commit()

    # Transição válida
    assert await ContractStateMachine.transition(contract, ContractState.QUESTIONED, db_session) is True
    assert contract.status == ContractState.QUESTIONED.value

    # Transição inválida
    assert await ContractStateMachine.transition(contract, ContractState.EXECUTED, db_session) is False