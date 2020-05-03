from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.conference import Conference


class CRUDAuthor(CRUDBase):
    def get_by_name(self, db_session: Session, *, name: str) -> Optional[Conference]:
        return db_session.query(Conference).filter(Conference.name == name).first()


conference = CRUDAuthor(Conference)
