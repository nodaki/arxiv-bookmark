from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.paper_tag_link import PaperTagLink


class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, index=True)

    papers = relationship("Paper", secondary=PaperTagLink.__tablename__, back_populates="tags")
