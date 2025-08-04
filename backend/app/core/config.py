"""
app/core/config.py

Configurações centrais do sistema Minicontratos.
Utiliza Pydantic para validação e gerenciamento de variáveis de ambiente.
Inclui parâmetros para banco de dados, Supabase, MCP, segurança e tunáveis do sistema.
"""

from pydantic import BaseSettings, PostgresDsn, Field
from typing import Optional

class Settings(BaseSettings):
    # Configuração do servidor
    API_HOST: str = Field("0.0.0.0", description="Host da API")
    API_PORT: int = Field(8000, description="Porta da API")
    DEBUG: bool = Field(False, description="Modo de depuração")

    # Banco de dados principal (PostgreSQL/Supabase)
    DB_URL: PostgresDsn = Field(..., env="POSTGRES_URL", description="URL do banco de dados principal")
    SUPABASE_URL: str = Field(..., env="SUPABASE_URL", description="URL do projeto Supabase")
    SUPABASE_KEY: str = Field(..., env="SUPABASE_KEY", description="Chave de API do Supabase")

    # Segurança
    SECRET_KEY: str = Field("changeme", description="Chave secreta para JWT")
    ALGORITHM: str = Field("HS256", description="Algoritmo de criptografia JWT")
    TOKEN_EXPIRE_MINUTES: int = Field(60 * 24, description="Tempo de expiração do token (minutos)")

    # Integração Model Context Protocol (MCP)
    MCP_ENDPOINT: str = Field("https://api.minicontratos.com/mcp", description="Endpoint MCP")
    OPENAI_API_KEY: Optional[str] = Field(None, env="OPENAI_API_KEY", description="Chave de API OpenAI (GPT Custom)")
    
    # Diretórios internos
    DOCS_PATH: str = Field("docs/", description="Diretório de documentação")
    CRON_PATH: str = Field("cron/", description="Diretório de scripts periódicos")
    ARMOR_PATH: str = Field("app/armor/", description="Blindagem do sistema")
    RULES_PATH: str = Field("rules/", description="Contratos-regra do sistema")

    # Outros parâmetros tunáveis
    MAX_IDEA_COST: float = Field(100000.0, description="Custo máximo permitido para ideias")
    MAX_CONTRACT_VALUE: float = Field(1000000.0, description="Valor máximo permitido para contratos")
    VOTE_SCALE: int = Field(10, description="Escala máxima de votos")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instância global de settings
settings = Settings()