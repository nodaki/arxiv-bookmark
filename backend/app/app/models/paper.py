from sqlalchemy import Boolean, Column, Integer, String, TEXT, DATETIME
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.paper_author_link import PaperAuthorLink
from app.models.paper_tag_link import PaperTagLink
from app.models.paper_conference_link import PaperConferenceLink


class Paper(Base):
    id = Column(Integer, primary_key=True, index=True)
    arxiv_id = Column(String(16), index=True, unique=True)
    title = Column(TEXT)
    published = Column(DATETIME)
    updated = Column(DATETIME)
    is_new = Column(Boolean())
    summary = Column(TEXT)
    arxiv_url = Column(String(127))
    pdf_url = Column(String(127))
    arxiv_primary_category = Column(String(127))
    arxiv_comment = Column(TEXT)
    affiliation = Column(String(127))
    journal_reference = Column(TEXT)
    doi = Column(String(127))

    authors = relationship("Author", secondary=PaperAuthorLink.__tablename__, back_populates="papers")
    tags = relationship("Tag", secondary=PaperTagLink.__tablename__, back_populates="papers")
    conferences = relationship("Conference", secondary=PaperConferenceLink.__tablename__, back_populates="papers")
