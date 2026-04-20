
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):

    prompt: str = Field(..., description="User message to LLM")
    system: str | None = Field(None, description="Optional system instruction")
    max_history: int = Field(10, ge=1, le=50, description="Max history messages")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Model temperature")


class ChatResponse(BaseModel):

    answer: str


class ChatMessageResponse(BaseModel):

    id: int
    role: str
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)