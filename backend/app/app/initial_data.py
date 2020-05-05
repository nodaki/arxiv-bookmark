import logging

from app.db.init_db import init_db
from app.db.session import db_session
from app.worker.tasks.papers import create_and_update_papers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init():
    init_db(db_session)
    create_and_update_papers()


def main():
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
