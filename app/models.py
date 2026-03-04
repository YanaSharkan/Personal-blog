from pydantic import BaseModel

from typing import Optional


# In-memory storage
ARTICLES = []


# Pydantic models
class Article(BaseModel):
    id: str
    title: str
    content: str
    created_at: str
    updated_at: Optional[str] = None


class ArticleCreate(BaseModel):
    title: str
    content: str
    created_at: str
    updated_at: Optional[str] = None


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    updated_at: Optional[str] = None
