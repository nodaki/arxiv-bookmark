from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.paper import Paper as DBPaper
from app.models.user import User as DBUser


class BookmarkBase(BaseModel):
    user_id: Optional[int] = None
    paper_id: Optional[int] = None


class BookmarkBaseInDB(BookmarkBase):
    user_id: int = None
    paper_id: int = None
    created_at: datetime = datetime.now()
    user: Optional[DBUser] = None
    paper: Optional[DBPaper] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class BookmarkCreate(BookmarkBaseInDB):
    pass


class BookmarkUpdate(BookmarkBaseInDB):
    pass


class Bookmark(BookmarkBaseInDB):
    pass


class BookmarkInDB(BookmarkBaseInDB):
    pass
