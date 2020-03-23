from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.bookmark import Bookmark
from app.schemas.bookmark import BookmarkCreate


class CRUDBookmark(CRUDBase):
    def create(self, db_session: Session, *, obj_in: BookmarkCreate) -> Bookmark:
        db_obj = self.model(**obj_in.dict())
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def get_bookmark(self, db_session: Session, *, user_id: int, paper_id: int) -> Optional[Bookmark]:
        return db_session.query(Bookmark).filter(Bookmark.user_id == user_id, Bookmark.paper_id == paper_id).first()

    def remove_bookmark(self, db_session: Session, *, user_id: int, paper_id: int) -> Optional[Bookmark]:
        bookmark = db_session.query(Bookmark).filter(Bookmark.user_id == user_id, Bookmark.paper_id == paper_id).first()
        db_session.delete(bookmark)
        db_session.commit()
        return bookmark


bookmark = CRUDBookmark(Bookmark)
