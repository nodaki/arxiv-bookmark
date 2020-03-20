from app.models.paper import Paper as DBPaper
from app.schemas.paper import Paper


def convert_paperindb_to_paper(paper_in_db: DBPaper) -> Paper:
    paper = Paper(
            id=paper_in_db.id,
            arxiv_id=paper_in_db.arxiv_id,
            title=paper_in_db.title,
            is_new=paper_in_db.is_new,
            summary=paper_in_db.summary,
            arxiv_url=paper_in_db.arxiv_url,
            pdf_url=paper_in_db.pdf_url,
            arxiv_primary_category=paper_in_db.arxiv_primary_category,
            arxiv_comment=paper_in_db.arxiv_comment,
            affiliation=paper_in_db.affiliation,
            journal_reference=paper_in_db.journal_reference,
            doi=paper_in_db.doi,
            published=paper_in_db.published.isoformat(),
            updated=paper_in_db.updated.isoformat(),
            authors=[author.name for author in paper_in_db.authors],
            tags=[tag.name for tag in paper_in_db.tags],
            conferences=[conference.name for conference in paper_in_db.conferences]
    )
    return paper
