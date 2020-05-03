from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class PaperTagLink(Base):
    paper_id = Column(Integer, ForeignKey("paper.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tag.id"), primary_key=True)
