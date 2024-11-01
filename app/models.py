
# app/models.py
from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    language: str = "en"

class ChatResponse(BaseModel):
    answer: str
