from app.models.paper import Paper as DBPaper
from app.schemas.paper import Paper, PaperInDB


def convert_paperindb_to_paper(paper_in_db: DBPaper) -> Paper:
    paper_data = PaperInDB.from_orm(paper_in_db).dict()
    # Convert datetime to isoformat(str)
    paper_data["published"] = paper_data["published"].isoformat()
    paper_data["updated"] = paper_data["updated"].isoformat()
    paper = Paper(**paper_data)
    return paper
