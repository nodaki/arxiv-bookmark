from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.paper_conference_link import PaperConferenceLink


class Conference(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True)

    papers = relationship("Paper", secondary=PaperConferenceLink.__tablename__, back_populates="conferences")
