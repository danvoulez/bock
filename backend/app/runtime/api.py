from fastapi import APIRouter, Request
from app.runtime.runtime import MinicontratosRuntime

router = APIRouter()

@router.post("/runtime/execute/{rule_id}")
async def execute_runtime_rule(rule_id: str, context: dict, request: Request):
    tenant_id = request.headers.get('X-Tenant-ID', 'default')
    runtime = MinicontratosRuntime(tenant_id)
    result = runtime.execute_rule(rule_id, context)
    return {"result": result}

@router.post("/runtime/reload")
async def reload_runtime(request: Request):
    tenant_id = request.headers.get('X-Tenant-ID', 'default')
    runtime = MinicontratosRuntime(tenant_id)
    runtime.reload_rules()
    return {"status": "reloaded"}