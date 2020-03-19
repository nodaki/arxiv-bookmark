from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.schemas.paper import Paper

router = APIRouter()


@router.get("/", response_model=List[Paper])
def read_papers(
        db: Session = Depends(get_db),
        skip: int = Query(default=0, description="skip"),
        limit: int = Query(default=10, description="limit")
):
    """
    Read papers.
    """
    papers_in_db = crud.paper.get_multi(db, skip=skip, limit=limit)
    papers = []
    for paper_in_db in papers_in_db:
        paper = Paper(
                arxiv_id=paper_in_db.arxiv_id,
                title=paper_in_db.title,
                is_new=paper_in_db.is_new,
                summary=paper_in_db.summary,
                arxiv_url=paper_in_db.arxiv_url,
                pdf_url=paper_in_db.pdf_url,
                arxiv_primary_category=paper_in_db.arxiv_primary_category,
                arxiv_comment=paper_in_db.arxiv_comment,
                affiliation=paper_in_db.affiliation,
                journal_reference=paper_in_db.journal_reference,
                doi=paper_in_db.doi,
                published=paper_in_db.published.isoformat(),
                updated=paper_in_db.updated.isoformat(),
                authors=[author.name for author in paper_in_db.authors],
                tags=[tag.name for tag in paper_in_db.tags]
        )
        papers.append(paper)
    return papers
