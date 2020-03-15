from sqlalchemy import Boolean, Column, Integer, String, TEXT, DATETIME

from app.db.base_class import Base


class Paper(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    published = Column(DATETIME)
    updated = Column(DATETIME)
    is_new = Column(Boolean())
    summary = Column(TEXT)
    arxiv_url = Column(String)
    pdf_url = Column(String)
    arxiv_primary_category = Column(String)
    arxiv_comment = Column(String)
    affiliation = Column(String)
    journal_reference = Column(String)
    doi = Column(String)
