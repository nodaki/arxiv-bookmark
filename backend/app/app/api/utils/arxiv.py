from typing import List

import arxiv

from app.core import config
from app.schemas.paper import Paper


def get_papers_using_arxiv_api(category: List[str],
                               start: int,
                               max_results: int) -> List[Paper]:
    """
    Get papers using arxiv API.

    Args:
        category: List of search categories.
        start: Start number.
        max_results: Max results.

    Returns: List of Paper.

    """
    search_categories = "+OR+".join(map(lambda x: "cat:" + x, category))
    entries = arxiv.query(query=search_categories, max_results=max_results, start=start, sort_by="lastUpdatedDate",
                          sort_order="descending")
    papers = []
    for entry in entries:
        entry["arxiv_id"] = entry["id"].split("/")[-1].split("v")[0]
        entry["tags"] = [t.term for t in entry["tags"]]
        entry["arxiv_primary_category"] = entry["arxiv_primary_category"]["term"]
        entry["title"] = entry["title"].replace("\n", "")
        entry["summary"] = entry["summary"].replace("\n", "")
        entry["is_new"] = entry["published"] == entry["updated"]
        # Conference tag
        conferences = []
        if entry["arxiv_comment"]:
            for c in config.CONFERENCE_LIST:
                if c in entry["arxiv_comment"].upper():
                    conferences.append(c)
        entry["conferences"] = conferences
        papers.append(Paper(**entry))
    return papers
