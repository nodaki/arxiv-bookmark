from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.tag import Tag


class CRUDTag(CRUDBase):
    def get_by_name(self, db_session: Session, *, name: str) -> Optional[Tag]:
        return db_session.query(Tag).filter(Tag.name == name).first()


tag = CRUDTag(Tag)
