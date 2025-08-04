"""
app/armor/audit_logger.py

Módulo de auditoria detalhada. Registra todas ações críticas, tentativas suspeitas, rollbacks e operações administrativas.
Pode ser integrado com banco, arquivo ou serviço externo (ex: Supabase).
"""

from datetime import datetime

# Simulação: escreve em arquivo local. Em produção, integrar com banco/audit trail.

def log_system_action(action: str, details: str, level: str = "INFO"):
    timestamp = datetime.utcnow().isoformat()
    log_line = f"{timestamp} | {level} | {action} | {details}\n"
    # Escreve em arquivo local (app/logs/audit.log)
    try:
        with open("app/logs/audit.log", "a") as f:
            f.write(log_line)
    except Exception:
        # Fallback: print no console
        print(log_line)