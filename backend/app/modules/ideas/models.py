from sqlalchemy import Column, String, Float, DateTime, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid

class Idea(Base):
    __tablename__ = "ideas"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String(36), nullable=False, index=True)
    title = Column(String(120), nullable=False)
    description = Column(Text)
    priority_data = Column(JSON)
    cost_data = Column(JSON)
    workflow_state = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    author_id = Column(UUID)