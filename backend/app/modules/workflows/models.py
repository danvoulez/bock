"""
app/modules/workflows/models.py

Modelos SQLAlchemy para Workflows, Steps, e integração com ideias/contratos.
"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid
from datetime import datetime

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String(36), nullable=False, index=True)
    name = Column(String(80), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workflow_id = Column(UUID(as_uuid=True), ForeignKey("workflows.id"), nullable=False)
    item_id = Column(UUID(as_uuid=True), nullable=False)  # Pode ser ideia ou contrato
    item_type = Column(String(20), nullable=False)  # 'idea' ou 'contract'
    step_order = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)