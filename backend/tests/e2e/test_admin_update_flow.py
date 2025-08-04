import pytest
from app.cicd.update_handler import CodeUpdateHandler
from unittest.mock import patch

def test_full_update_flow():
    handler = CodeUpdateHandler()
    with patch("subprocess.run") as mock_run:
        result = handler.apply_update("git pull origin main")
        assert result["status"] == "success"

def test_update_with_failure():
    handler = CodeUpdateHandler()
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = Exception("Erro de teste")
        with patch("app.armor.auto_rollback.AutoRollbackSystem") as mock_rollback:
            result = handler.apply_update("comando inválido")
            mock_rollback.db_rollback.assert_called()
            mock_rollback.code_rollback.assert_called()
            assert result["status"] == "error"