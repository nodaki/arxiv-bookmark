from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.paper import Paper


class CRUDPaper(CRUDBase):
    def get_by_arxiv_id(self, db_session: Session, *, arxiv_id: str) -> Optional[Paper]:
        return db_session.query(Paper).filter(Paper.arxiv_id == arxiv_id).first()


paper = CRUDPaper(Paper)
