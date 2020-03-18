import datetime
import logging

from app import crud
from app.core import config
from app.db.session import db_session
from app.schemas.paper import PaperUpdate
from app.worker.celery import app
from app.worker.utils import arxiv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.task(name="worker.papers.create_and_update_papers")
def create_and_update_papers():
    base_date = datetime.date.today() - datetime.timedelta(days=-1)
    previous_date = datetime.date.today() + datetime.timedelta(days=-2)
    papers = arxiv.search(
            categories=config.SEARCH_CATEGORIES,
            sort_by="lastUpdatedDate",
            sort_order="ascending",
            previous_date=previous_date,
            base_date=base_date
    )

    logger.info(f"Today's updated papers: {len(papers)}")
    for paper_in in papers:
        paper = crud.paper.get_by_arxiv_id(db_session=db_session, arxiv_id=paper_in.arxiv_id)
        if paper:
            if paper.updated == paper_in.updated:
                continue
            else:
                # Update the paper
                setattr(paper_in, "id", paper.id)
                crud.paper.update(db_session=db_session, db_obj=paper, obj_in=PaperUpdate(**paper_in.dict()))
                logger.info(f"Update {paper.arxiv_id}")
        else:
            # Create the paper
            crud.paper.create(db_session=db_session, obj_in=paper_in)
            logger.info(f"Create {paper_in.arxiv_id}")


if __name__ == '__main__':
    pass
