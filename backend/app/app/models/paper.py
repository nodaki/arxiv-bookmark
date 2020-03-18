from sqlalchemy import Boolean, Column, Integer, String, TEXT, DATETIME

from app.db.base_class import Base


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
    arxiv_primary_category = Column(String(16))
    arxiv_comment = Column(TEXT)
    affiliation = Column(String(127))
    journal_reference = Column(String(127))
    doi = Column(String(127))
