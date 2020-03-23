from sqlalchemy import Column, Integer, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Bookmark(Base):
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    paper_id = Column(Integer, ForeignKey("paper.id"), primary_key=True)
    created_at = Column(DATETIME)

    user = relationship("User", back_populates="bookmarks")
    paper = relationship("Paper", back_populates="bookmarks")
