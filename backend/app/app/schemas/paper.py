from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.models.author import Author
from app.models.conference import Conference
from app.models.tag import Tag


class PaperBase(BaseModel):
    arxiv_id: str
    title: str
    is_new: bool
    summary: str
    arxiv_url: str
    pdf_url: str
    arxiv_primary_category: str
    arxiv_comment: Optional[str] = None
    affiliation: Optional[str] = None
    journal_reference: Optional[str] = None
    doi: Optional[str] = None


class PaperBaseInDB(PaperBase):
    id: int = None
    published: datetime
    updated: datetime

    class Config:
        orm_mode = True


class PaperCreate(PaperBaseInDB):
    authors: Optional[List[Author]] = None
    tags: Optional[List[Tag]] = None
    conferences: Optional[List[Conference]] = None

    class Config:
        arbitrary_types_allowed = True


class PaperUpdate(PaperBaseInDB):
    authors: Optional[List[Author]] = None
    tags: Optional[List[Tag]] = None
    conferences: Optional[List[Conference]] = None

    class Config:
        arbitrary_types_allowed = True


class Paper(PaperBase):
    id: int
    published: str
    updated: str
    authors: Optional[List[str]] = None
    conferences: Optional[List[str]] = None
    tags: Optional[List[str]] = None

    class Config:
        orm_mode = True


class PaperInDB(PaperBaseInDB):
    pass
