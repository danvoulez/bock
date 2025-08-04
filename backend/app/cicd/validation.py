"""
app/cicd/validation.py

Validação sintática e semântica de atualizações de código/configuração.
Verifica padrões, regras de segurança, limitações e integra com audit trail.
"""

import re

def validate_update(update_command: str) -> bool:
    """
    Valida update antes de execução:
    - Permite apenas comandos de git, docker-compose e alembic seguros.
    - Bloqueia comandos suspeitos ou fora do padrão.
    - Pode ser expandido para validação semântica mais profunda.
    """
    allowed_patterns = [
        r"^git (pull|fetch|merge|checkout|reset --hard [\w@{}]+)$",
        r"^docker-compose (up -d --build|down|restart)$",
        r"^alembic (upgrade head|downgrade .+)$",
        r"^pytest tests/?$"
    ]
    for pat in allowed_patterns:
        if re.match(pat, update_command.strip()):
            return True
    return False