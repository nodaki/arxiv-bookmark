from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class PaperAuthorLink(Base):
    paper_id = Column(Integer, ForeignKey("paper.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)
