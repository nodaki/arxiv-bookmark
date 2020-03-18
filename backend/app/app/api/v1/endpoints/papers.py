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
        setattr(paper_in_db, "published", paper_in_db.published.isoformat())
        setattr(paper_in_db, "updated", paper_in_db.updated.isoformat())
        setattr(paper_in_db, "authors", ["author1", "author2"])
        setattr(paper_in_db, "tags", [paper_in_db.arxiv_primary_category])
        papers.append(Paper.from_orm(paper_in_db))
    return papers
