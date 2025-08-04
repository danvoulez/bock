"""
app/core/database.py

Configuração da conexão assíncrona com o banco de dados (PostgreSQL/Supabase).
Define a base ORM, engine assíncrono, sessionmaker e dependência FastAPI para obter sessões.
Inclui inicialização de schemas e integração futura com Supabase.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

Base = declarative_base()

engine = create_async_engine(settings.DB_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    """
    Dependência FastAPI para obter uma sessão assíncrona do banco.
    """
    async with AsyncSessionLocal() as session:
        yield session

def init_db():
    """
    Inicializa as tabelas no banco de dados.
    Para uso em scripts standalone.
    """
    import asyncio
    async def _run():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    asyncio.run(_run())