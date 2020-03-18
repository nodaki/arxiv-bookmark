from datetime import date, datetime
from typing import List

import feedparser

from app.schemas.paper import PaperCreate


def search(categories: List[str],
           sort_by: str,
           sort_order: str,
           previous_date: date,
           base_date: date,
           start: int = 0,
           max_results: int = None) -> List[PaperCreate]:
    if not max_results:
        max_results = 1000
    search_categories = "+OR+".join(map(lambda x: "cat:" + x, categories))
    root_url = "http://export.arxiv.org/api/"
    query = f"search_query=({search_categories})+AND+" \
            f"lastUpdatedDate:[{previous_date.strftime('%Y%m%d')}0000+TO+{base_date.strftime('%Y%m%d')}0000]" \
            f"&sortBy={sort_by}&sortOrder={sort_order}&start={start}&max_results={max_results}"
    url = root_url + "query?" + query
    feed = feedparser.parse(url)
    papers = []
    for entry in feed.entries:
        entry["pdf_url"] = None
        for link in entry["links"]:
            if "title" in link and link["title"] == "pdf":
                entry["pdf_url"] = link["href"]
        entry["affiliation"] = entry.pop("arxiv_affiliation", "None")

        entry["arxiv_url"] = entry.pop("link")
        entry["title"] = entry["title"].replace("\n", "")
        entry["summary"] = entry["summary"].replace("\n", "")
        entry["authors"] = [d["name"] for d in entry["authors"]]
        if "arxiv_comment" in entry:
            entry["arxiv_comment"] = entry["arxiv_comment"].rstrip("\n")
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
        entry["arxiv_id"] = entry["id"].split("/")[-1].split("v")[0]
        entry["id"] = None
        entry["arxiv_primary_category"] = entry["arxiv_primary_category"]["term"]
        entry["tags"] = [t.term for t in entry["tags"]]
        entry["is_new"] = entry["published"] == entry["updated"]
        entry["published"] = datetime(*entry.pop("published_parsed")[:6])
        entry["updated"] = datetime(*entry.pop("updated_parsed")[:6])
        papers.append(PaperCreate(**entry))
    return papers
