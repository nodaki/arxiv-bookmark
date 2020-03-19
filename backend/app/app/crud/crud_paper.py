from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app import crud
from app.crud.base import CRUDBase
from app.models.author import Author
from app.models.paper import Paper
from app.schemas.paper import PaperCreate, PaperInDB


class CRUDPaper(CRUDBase):
    def get_by_arxiv_id(self, db_session: Session, *, arxiv_id: str) -> Optional[Paper]:
        return db_session.query(Paper).filter(Paper.arxiv_id == arxiv_id).first()

    def get_multi(self, db_session: Session, *, skip=0, limit=10) -> List[Paper]:
        return db_session.query(Paper).order_by(desc(Paper.updated)).offset(skip).limit(limit).all()

    def create(self, db_session: Session, *, obj_in: PaperCreate) -> Paper:
        obj_in_data = PaperInDB(**jsonable_encoder(obj_in))
        db_obj = self.model(**jsonable_encoder(obj_in_data))
        # Relation with authors
        for author_name in obj_in.authors:
            author = crud.author.get_by_name(db_session=db_session, name=author_name)
            if not author:
                author = Author(name=author_name)
            db_obj.authors.append(author)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj


paper = CRUDPaper(Paper)
