from pydantic import BaseModel, Field
from typing import Optional, List
import uuid

class IdeaCreate(BaseModel):
    title: str = Field(..., max_length=120)
    description: str
    priority: float = 5.0
    cost_data: Optional[dict] = None
    author_id: uuid.UUID

class VoteCreate(BaseModel):
    score: float = Field(..., ge=1, le=10)
    voter_id: uuid.UUID

class IdeaResponse(IdeaCreate):
    id: uuid.UUID
    priority_data: dict
    workflow_state: str