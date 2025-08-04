"""
app/modules/contracts/models.py

Modelos SQLAlchemy para contratos, despachos, acionamentos, penalidades e integração multitenant.
Inclui workflow de estados, testemunhas, mecanismos de despacho e auditoria.
"""

from sqlalchemy import Column, String, Text, Float, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid

CONTRACT_STATUS = ('ATIVO', 'CUMPRIDO', 'QUESTIONADO', 'PENALIZADO', 'DESPACHADO', 'ARQUIVADO')

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String(36), index=True, nullable=False)
    title = Column(String(120), nullable=False)
    description = Column(Text)
    author_id = Column(UUID(as_uuid=True), ForeignKey("people.id"), nullable=False)
    witness_id = Column(UUID(as_uuid=True), ForeignKey("people.id"))
    value = Column(Float, default=0.0)
    deadline = Column(DateTime)
    penalty = Column(Text)
    normal_consequence = Column(Text)
    questioning_procedure = Column(Text)
    penalty_procedure = Column(Text)
    status = Column(String(24), default="ATIVO")
    triggered_at = Column(DateTime)
    dispatched_to = Column(UUID(as_uuid=True), ForeignKey("people.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    workflow_state = Column(String(50), default="ATIVO")
    rule_definition = Column(JSONB, default=dict)

    dispatches = relationship("Dispatch", backref="contract", cascade="all, delete-orphan", lazy="dynamic")

class Dispatch(Base):
    __tablename__ = "dispatches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contract_id = Column(UUID(as_uuid=True), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False)
    dispatched_to = Column(UUID(as_uuid=True), ForeignKey("people.id"))
    reason = Column(Text)
    status = Column(String(24), default="pending")  # pending, accepted, rejected, escalated
    created_at = Column(DateTime, default=datetime.utcnow)
    logline = Column(JSONB, default=dict)

class Penalty(Base):
    __tablename__ = "penalties"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contract_id = Column(UUID(as_uuid=True), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False)
    applied_at = Column(DateTime, default=datetime.utcnow)
    amount = Column(Float, default=0.0)
    reason = Column(Text)
    logline = Column(JSONB, default=dict)