"""
app/modules/registry/objects/models.py

Modelo SQLAlchemy para Objetos no Registry. Inclui campos avançados para arquivos, tokens, links externos, metadados e multitenancy.
"""

from sqlalchemy import Column, String, Text, DateTime, Boolean, Float, ForeignKey, JSON, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.core.database import Base
import uuid
from datetime import datetime

class Object(Base):
    __tablename__ = "objects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(120), nullable=False)
    alias = Column(String(120))
    type = Column(String(50), nullable=False)
    subtype = Column(String(50))
    category = Column(String(50))
    tenant_id = Column(String(36), nullable=False, index=True)
    ghost = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)

    filename = Column(String(120))
    mimetype = Column(String(50))
    storage_path = Column(String(256), unique=True)
    size_bytes = Column(Integer)
    hash_sha256 = Column(String(64))

    owner_id = Column(UUID(as_uuid=True))
    linked_to = Column(UUID(as_uuid=True))
    access_scope = Column(JSONB)
    access_tokens = Column(JSONB)

    rendering_uri = Column(String(256))
    appearance_uri = Column(String(256))
    preview_text = Column(String(120))
    transcription_uri = Column(String(256))

    location = Column(String(128))
    condition = Column(String(50))
    acquisition_date = Column(DateTime)
    expiration_date = Column(DateTime)

    external_ids = Column(JSONB)
    external_links = Column(JSONB)
    linked_contracts = Column(JSONB)

    embedding = Column(JSONB)
    style_tokens = Column(JSONB)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)