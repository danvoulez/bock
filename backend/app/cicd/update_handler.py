"""
app/cicd/update_handler.py

Handler de atualizações de código/configuração.
Integra com mecanismos anti-humano, auto-rollback, validação e pipeline de testes.
Permite atualização e rollback via ChatGPT/MCP para admins autorizados.
"""

import subprocess
import git
from app.armor.anti_human import HumanErrorProtection
from app.armor.auto_rollback import AutoRollbackSystem
from app.armor.audit_logger import log_system_action
from app.cicd.validation import validate_update

class CodeUpdateHandler:
    def __init__(self):
        self.repo = git.Repo(".")  # Assume execução na raiz do repo

    def apply_update(self, update_command: str, user_id: str):
        """
        Aplica atualização de código/configuração de forma segura.
        Executa testes, validações e integra com rollback.
        """
        # Valida comando perigoso
        if not HumanErrorProtection.validate_destructive_command(update_command):
            log_system_action("CICD_BLOCKED", f"Comando bloqueado por anti-humano: {update_command}", level="ERROR")
            return {"status": "error", "message": "Comando bloqueado por segurança"}

        # Rate limiting por usuário
        if not HumanErrorProtection.action_speed_limiter(user_id):
            log_system_action("CICD_BLOCKED", f"Ação muito rápida por {user_id}", level="WARNING")
            return {"status": "error", "message": "Ação bloqueada por excesso de requisições"}

        # Validação semântica e sintática
        if not validate_update(update_command):
            log_system_action("CICD_BLOCKED", f"Update inválido: {update_command}", level="ERROR")
            return {"status": "error", "message": "Update inválido ou não autorizado"}

        try:
            # Teste automatizado antes do update
            subprocess.run(["pytest", "tests/"], check=True)
            log_system_action("CICD_TESTS", "Testes automatizados passaram")

            # Executa o comando de update
            self.repo.git.execute(update_command)
            log_system_action("CICD_UPDATE", f"Update aplicado: {update_command}")

            # Migrações de banco (se necessário)
            subprocess.run(["alembic", "upgrade", "head"], check=True)
            log_system_action("CICD_DB_MIGRATION", "Migração de banco concluída")

            return {"status": "success", "message": "Update aplicado com sucesso"}
        except Exception as e:
            # Rollback automático em caso de erro
            log_system_action("CICD_ERROR", str(e), level="ERROR")
            AutoRollbackSystem.db_rollback("previous")
            AutoRollbackSystem.code_rollback("HEAD@{1}")
            return {"status": "error", "message": f"Erro ao aplicar update: {e}, rollback realizado"}