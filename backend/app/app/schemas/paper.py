from typing import List

from pydantic import BaseModel


class PaperBase(BaseModel):
    arxiv_id: str
    title: str
    is_new: bool
    summary: str
    arxiv_url: str
    pdf_url: str
    arxiv_primary_category: str
    arxiv_comment: str = None
    affiliation: str = None
    journal_reference: str = None
    doi: str = None


class Paper(PaperBase):
    published: str
    updated: str
    authors: List[str]
    conferences: List[str]
    tags: List[str]
