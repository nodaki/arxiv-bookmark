from typing import List

from fastapi import APIRouter, Query

from app.api.utils.arxiv import get_papers_using_arxiv_api
from app.schemas.paper import Paper

router = APIRouter()


@router.get("/", response_model=List[Paper])
def read_papers(category: List[str] = Query(default=["cs.CV"], description="Search categories"),
                start: int = Query(default=0, description="Start number"),
                max_results: int = Query(default=10, description="Max results")):
    """
    Read papers.
    """
    return get_papers_using_arxiv_api(category=category, start=start, max_results=max_results)
