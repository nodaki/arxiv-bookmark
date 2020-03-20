from datetime import date, datetime
from typing import List, TypeVar, Generator

import feedparser

from app import crud
from app.core import config
from app.crud.base import CRUDBase
from app.db.base import Base
from app.db.session import db_session
from app.models.author import Author
from app.models.conference import Conference
from app.models.tag import Tag
from app.schemas.paper import PaperCreate

CRUDType = TypeVar("CRUDType", bound=CRUDBase)
ModelType = TypeVar("ModelType", bound=Base)


def create_link_model(crud_base: CRUDType, model: ModelType, name_list: List[str]):
    records = []
    for name in name_list:
        record = crud_base.get_by_name(db_session=db_session, name=name)
        if not record:
            record = model(name=name)
        records.append(record)
    return records


def search(categories: List[str],
           sort_by: str,
           sort_order: str,
           previous_date: date,
           base_date: date,
           start: int = 0,
           max_results: int = None) -> Generator[PaperCreate, None, None]:
    if not max_results:
        max_results = 1000
    search_categories = "+OR+".join(map(lambda x: "cat:" + x, categories))
    root_url = "http://export.arxiv.org/api/"
    query = f"search_query=({search_categories})+AND+" \
            f"lastUpdatedDate:[{previous_date.strftime('%Y%m%d')}0000+TO+{base_date.strftime('%Y%m%d')}0000]" \
            f"&sortBy={sort_by}&sortOrder={sort_order}&start={start}&max_results={max_results}"
    url = root_url + "query?" + query
    feed = feedparser.parse(url)
    for entry in feed.entries:
        if not entry["arxiv_primary_category"]["term"] in config.SEARCH_CATEGORIES:
            continue
        else:
            entry["pdf_url"] = None
            for link in entry["links"]:
                if "title" in link and link["title"] == "pdf":
                    entry["pdf_url"] = link["href"]
            entry["affiliation"] = entry.pop("arxiv_affiliation", None)

            entry["arxiv_url"] = entry.pop("link")
            entry["title"] = entry["title"].replace("\n", "")
            entry["summary"] = entry["summary"].replace("\n", "")
            entry["authors"] = create_link_model(crud.author, Author, [a["name"] for a in entry["authors"]])
            if "arxiv_comment" in entry:
                entry["arxiv_comment"] = entry["arxiv_comment"].replace("\n", "")
            else:
                entry["arxiv_comment"] = None
            if "arxiv_journal_ref" in entry:
                entry["journal_reference"] = entry.pop("arxiv_journal_ref")
            else:
                entry["journal_reference"] = None
            if "arxiv_doi" in entry:
                entry["doi"] = entry.pop("arxiv_doi")
            else:
                entry["doi"] = None
            entry["arxiv_id"] = entry.pop("id").split("/")[-1].split("v")[0]
            entry["arxiv_primary_category"] = entry["arxiv_primary_category"]["term"]
            entry["tags"] = create_link_model(crud.tag, Tag,
                                              [t.term for t in entry["tags"] if t.term in config.CATEGORY_LIST])
            entry["is_new"] = entry["published"] == entry["updated"]
            entry["published"] = datetime(*entry.pop("published_parsed")[:6])
            entry["updated"] = datetime(*entry.pop("updated_parsed")[:6])
            conferences = []
            if entry["arxiv_comment"]:
                for conference in config.CONFERENCE_LIST:
                    if conference in entry["arxiv_comment"].upper():
                        conferences.append(conference)
            entry["conferences"] = create_link_model(crud.conference, Conference, conferences)
            yield PaperCreate(**entry)
