from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.paper_author_link import PaperAuthorLink


class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, index=True)

    papers = relationship("Paper", secondary=PaperAuthorLink.__tablename__, back_populates="authors")
