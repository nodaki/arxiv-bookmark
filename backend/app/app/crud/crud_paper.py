from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.bookmark import Bookmark
from app.models.paper import Paper
from app.schemas.paper import PaperCreate, PaperUpdate, PaperInDB


class CRUDPaper(CRUDBase):
    def get_by_arxiv_id(self, db_session: Session, *, arxiv_id: str) -> Optional[Paper]:
        return db_session.query(Paper).filter(Paper.arxiv_id == arxiv_id).first()

    def get_multi(self, db_session: Session, *, skip=0, limit=10) -> List[Paper]:
        return db_session.query(Paper).order_by(desc(Paper.updated)).offset(skip).limit(limit).all()

    def get_bookmarked_papers(self, db_session: Session, *, user_id: int):
        return db_session.query(Paper) \
            .join(Paper.bookmarks) \
            .filter(Bookmark.user_id == user_id) \
            .order_by(Bookmark.created_at.desc()) \
            .all()

    def create(self, db_session: Session, *, obj_in: PaperCreate) -> Paper:
        obj_in_data = PaperInDB(**jsonable_encoder(obj_in))
        db_obj = self.model(**jsonable_encoder(obj_in_data))
        # Relation with authors, tags and conferences
        db_obj.authors = obj_in.authors
        db_obj.tags = obj_in.tags
        db_obj.conferences = obj_in.conferences
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def update(self, db_session: Session, *, db_obj: Paper, obj_in: PaperUpdate) -> Paper:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(skip_defaults=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        # Relation with authors, tags and conferences
        db_obj.authors = obj_in.authors
        db_obj.tags = obj_in.tags
        db_obj.conferences = obj_in.conferences
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj


paper = CRUDPaper(Paper)
