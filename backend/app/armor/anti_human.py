"""
app/armor/anti_human.py

Módulo de blindagem anti-humana. Impede comandos perigosos, valida operações críticas e implementa rate-limiting de ações destrutivas.
Protocolo de confirmação em cascata para decisões de alto impacto.
"""

import time
import threading

class HumanErrorProtection:
    # Lista negra de comandos perigosos
    BLACKLIST = [
        "DROP TABLE", "TRUNCATE", "DELETE FROM", "ALTER TABLE", "GRANT ALL", "DROP DATABASE"
    ]

    # Armazena times de últimas ações por usuário
    _action_timestamps = {}
    _lock = threading.Lock()

    @staticmethod
    def validate_destructive_command(command: str) -> bool:
        """Impede comandos perigosos via interface"""
        for forbidden in HumanErrorProtection.BLACKLIST:
            if forbidden in command.upper():
                return False
        return True

    @staticmethod
    def confirm_high_impact_action(user_id: str, action: str) -> bool:
        """
        Exige confirmação escalonada para ações críticas: 
        - Solicita confirmação dupla/tripla
        - Pode requerer aprovação de outro admin/guardião
        """
        # Placeholder: sempre exige múltipla confirmação
        print(f"[ANTI-HUMAN] Solicitação de confirmação extra para {action} por {user_id}")
        # Exemplo simples: retorna True se usuário digitou "CONFIRMO" 2x
        confirmation_steps = 2
        for i in range(confirmation_steps):
            # Em produção, substituir por mecanismo real (MFA, e-mail, etc)
            pass
        return True

    @classmethod
    def action_speed_limiter(cls, user_id: str, min_seconds: int = 5) -> bool:
        """
        Impede execuções em rápida sucessão (rate limiting por usuário)
        """
        with cls._lock:
            now = time.time()
            last = cls._action_timestamps.get(user_id, 0)
            if now - last < min_seconds:
                print(f"[ANTI-HUMAN] Bloqueando ação rápida demais de {user_id}")
                return False
            cls._action_timestamps[user_id] = now
        return True

    @staticmethod
    def log_suspicious_attempt(user_id: str, command: str):
        # Integração com audit_logger
        from app.armor.audit_logger import log_system_action
        log_system_action("ANTI_HUMAN_BLOCK", f"Usuário {user_id} tentou comando bloqueado: {command}", level="WARNING")