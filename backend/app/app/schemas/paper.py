from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.models.author import Author as DBAuthor
from app.models.conference import Conference as DBConference
from app.models.tag import Tag as DBTag
from app.schemas.author import Author
from app.schemas.conference import Conference
from app.schemas.tag import Tag


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
    authors: Optional[List[DBAuthor]] = None
    tags: Optional[List[DBTag]] = None
    conferences: Optional[List[DBConference]] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class PaperCreate(PaperBaseInDB):
    pass


class PaperUpdate(PaperBaseInDB):
    pass


class Paper(PaperBaseInDB):
    published: str = None
    updated: str = None
    authors: Optional[List[Author]] = None
    tags: Optional[List[Tag]] = None
    conferences: Optional[List[Conference]] = None


class PaperInDB(PaperBaseInDB):
    pass
