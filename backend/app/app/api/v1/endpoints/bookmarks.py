from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.models.user import User as DBUser
from app.schemas.bookmark import BookmarkCreate
from app.schemas.paper import Paper

router = APIRouter()


@router.post("/", response_model=Paper)
def create_bookmark(
        *,
        db: Session = Depends(get_db),
        paper_id: int = Body(...),
        user_id: int = Body(...),
        current_user: DBUser = Depends(get_current_active_user)

):
    bookmark = crud.bookmark.get_bookmark(db, user_id=user_id, paper_id=paper_id)
    if bookmark:
        raise HTTPException(
                status_code=400,
                detail="The bookmark already exists in the system.",
        )
    paper = crud.paper.get(db_session=db, id=paper_id)
    bookmark_in = BookmarkCreate(
            user_id=user_id,
            paper_id=paper_id,
            created_at=datetime.now(),
            user=current_user,
            paper=paper
    )
    bookmark = crud.bookmark.create(db_session=db, obj_in=bookmark_in)
    return paper


@router.delete("/", response_model=Paper)
def remove_bookmark(
        *,
        db: Session = Depends(get_db),
        user_id: int = Body(...),
        paper_id: int = Body(...),
        current_user: DBUser = Depends(get_current_active_user)
):
    bookmark = crud.bookmark.remove_bookmark(db, user_id=user_id, paper_id=paper_id)
    paper = crud.paper.get(db_session=db, id=bookmark.paper_id)
    return paper


@router.get("/my-bookmarks", response_model=List[Paper])
def get_my_bookmarks(
        *,
        db: Session = Depends(get_db),
        current_user: DBUser = Depends(get_current_active_user)
):
    return crud.paper.get_bookmarked_papers(db, user_id=current_user.id)
