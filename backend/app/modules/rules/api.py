from fastapi import APIRouter, Request, Depends
from app.modules.rules.logline_runtime import LogLineRuntime

router = APIRouter()

def get_tenant_id(request: Request):
    return request.headers.get("x-tenant-id", "default")

@router.post("/rules/evaluate/{rule_id}")
async def evaluate_rule(rule_id: str, context: dict, request: Request):
    tenant_id = get_tenant_id(request)
    runtime = LogLineRuntime(tenant_id)
    result = runtime.evaluate(rule_id, context)
    return {"result": result}

@router.post("/rules/reload")
async def reload_rules(request: Request):
    tenant_id = get_tenant_id(request)
    runtime = LogLineRuntime(tenant_id)
    runtime.reload()
    return {"status": "reloaded"}