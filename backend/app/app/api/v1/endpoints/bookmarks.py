from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.papers import convert_paperindb_to_paper
from app.api.utils.security import get_current_active_user
from app.models.user import User as DBUser
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate
from app.schemas.paper import Paper

router = APIRouter()


@router.post("/", response_model=Paper)
def create_bookmark(
        *,
        db: Session = Depends(get_db),
        bookmark_in: BookmarkCreate,
        current_user: DBUser = Depends(get_current_active_user)

):
    bookmark = crud.bookmark.get_bookmark(db, user_id=bookmark_in.user_id, paper_id=bookmark_in.paper_id)
    if bookmark:
        raise HTTPException(
                status_code=400,
                detail="The bookmark already exists in the system.",
        )
    bookmark = crud.bookmark.create(db_session=db, obj_in=bookmark_in)
    paper = convert_paperindb_to_paper(crud.paper.get(db_session=db, id=bookmark.paper_id))
    return paper


@router.delete("/", response_model=Paper)
def remove_bookmark(
        *,
        db: Session = Depends(get_db),
        bookmark_remove: BookmarkUpdate,
        current_user: DBUser = Depends(get_current_active_user)
):
    bookmark = crud.bookmark.remove_bookmark(db, user_id=bookmark_remove.user_id, paper_id=bookmark_remove.paper_id)
    paper = convert_paperindb_to_paper(crud.paper.get(db_session=db, id=bookmark.paper_id))
    return paper
