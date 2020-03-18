from typing import Optional, List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.paper import Paper


class CRUDPaper(CRUDBase):
    def get_by_arxiv_id(self, db_session: Session, *, arxiv_id: str) -> Optional[Paper]:
        return db_session.query(Paper).filter(Paper.arxiv_id == arxiv_id).first()

    def get_multi(self, db_session: Session, *, skip=0, limit=10) -> List[Paper]:
        return db_session.query(Paper).order_by(desc(Paper.updated)).offset(skip).limit(limit).all()


paper = CRUDPaper(Paper)
