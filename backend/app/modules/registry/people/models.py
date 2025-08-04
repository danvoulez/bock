"""
app/modules/registry/people/models.py

Modelo SQLAlchemy para Pessoas no Registry. Inclui todos campos essenciais, multitenancy, biometria, autenticação, presença, e metadados.
"""

from sqlalchemy import Column, String, Text, DateTime, Boolean, Float, ForeignKey, JSON, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.core.database import Base
import uuid
from datetime import datetime

class Person(Base):
    __tablename__ = "people"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String(36), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    phone = Column(String(30))
    role = Column(String(50))
    ghost = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)
    verification_level = Column(String(24))

    # Consentimento RGPD
    consent_data_processing = Column(Boolean)
    consent_marketing = Column(Boolean)
    consent_cookies = Column(Boolean)
    consent_terms_accepted = Column(Boolean)
    consent_consented_at = Column(DateTime)
    consent_ip_address = Column(String(64))

    # Documentos e identidade digital
    document_type = Column(String(24))
    nif = Column(String(32))
    citizen_card = Column(String(32))
    passport = Column(String(32))
    documents = Column(JSONB)
    wallet_uri = Column(String(128))
    linked_wallets = Column(JSONB)

    # Biometria
    face_embedding = Column(JSONB)
    voice_embedding = Column(JSONB)
    selfie_path = Column(String(256))
    voice_sample_path = Column(String(256))
    video_verification_path = Column(String(256))

    # Autenticação
    auth_tokens = Column(JSONB)
    mfa_enabled = Column(Boolean, default=False)
    access_scopes = Column(JSONB)
    last_login_at = Column(DateTime)

    # Presença e sessão
    last_seen = Column(DateTime)
    location = Column(String(128))
    status = Column(String(24))
    availability = Column(String(24))

    # RFID/NFC/UHF
    rfid_tag = Column(String(64))
    nfc_uid = Column(String(64))
    uhf_token = Column(String(64))
    last_tag_scan_at = Column(DateTime)
    tag_scan_uri = Column(String(256))

    # Metadados e rastreamento
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    source = Column(String(128))
    source_history = Column(JSONB)
    chatgpt_id = Column(String(128))
    detected_attributes = Column(JSONB)
    reputation = Column(Float, default=0.0)
    symbolic_tokens = Column(JSONB)