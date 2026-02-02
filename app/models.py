from pydantic import BaseModel

from typing import Optional


# In-memory storage
ARTICLES = []


# Pydantic models
class Article(BaseModel):
    id: str
    title: str
    content: str
    date: str


class ArticleCreate(BaseModel):
    title: str
    content: str
    date: str


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    date: Optional[str] = None
