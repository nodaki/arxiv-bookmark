from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class Bookmark(Base):
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    paper_id = Column(Integer, ForeignKey("paper.id"), primary_key=True)
