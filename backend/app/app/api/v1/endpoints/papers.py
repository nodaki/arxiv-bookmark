from typing import List

from fastapi import APIRouter, Query, Depends, Path
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.papers import convert_paperindb_to_paper
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
        papers.append(convert_paperindb_to_paper(paper_in_db))
    return papers


@router.get("/{paper_id}", response_model=Paper)
def read_paper_by_id(db: Session = Depends(get_db), paper_id: int = Path(default=1)):
    paper_in_db = crud.paper.get(db_session=db, id=paper_id)
    return convert_paperindb_to_paper(paper_in_db)
