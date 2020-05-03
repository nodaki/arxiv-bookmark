from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.author import Author


class CRUDAuthor(CRUDBase):
    def get_by_name(self, db_session: Session, *, name: str) -> Optional[Author]:
        return db_session.query(Author).filter(Author.name == name).first()


author = CRUDAuthor(Author)
