from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class PaperConferenceLink(Base):
    paper_id = Column(Integer, ForeignKey("paper.id"), primary_key=True)
    conference_id = Column(Integer, ForeignKey("conference.id"), primary_key=True)
