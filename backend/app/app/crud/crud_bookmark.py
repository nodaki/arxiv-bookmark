from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.bookmark import Bookmark


class CRUDBookmark(CRUDBase):
    def get_bookmark(self, db_session: Session, *, user_id: int, paper_id: int) -> Optional[Bookmark]:
        return db_session.query(Bookmark).filter(Bookmark.user_id == user_id, Bookmark.paper_id == paper_id).first()

    def remove_bookmark(self, db_session: Session, *, user_id: int, paper_id: int) -> Optional[Bookmark]:
        bookmark = db_session.query(Bookmark).filter(Bookmark.user_id == user_id, Bookmark.paper_id == paper_id).first()
        db_session.delete(bookmark)
        db_session.commit()
        return bookmark


bookmark = CRUDBookmark(Bookmark)
