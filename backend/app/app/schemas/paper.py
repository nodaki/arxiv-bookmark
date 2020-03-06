from datetime import datetime
from typing import List

from pydantic import BaseModel


class PaperBase(BaseModel):
    arxiv_id: str
    title: str
    published: datetime
    updated: datetime
    summary: str
    arxiv_url: str
    pdf_url: str
    arxiv_primary_category: str
    arxiv_comment: str = None
    affiliation: str = None
    journal_reference: str = None
    doi: str = None


class Paper(PaperBase):
    authors: List[str]
    tags: List[str]
