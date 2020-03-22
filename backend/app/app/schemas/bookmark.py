from typing import Optional

from pydantic import BaseModel


class BookmarkBase(BaseModel):
    user_id: Optional[int] = None
    paper_id: Optional[int] = None


class BookmarkBaseInDB(BookmarkBase):
    user_id: int = None
    paper_id: int = None

    class Config:
        orm_mode = True


class BookmarkCreate(BookmarkBaseInDB):
    pass


class BookmarkUpdate(BookmarkBaseInDB):
    pass


class Bookmark(BookmarkBaseInDB):
    pass


class BookmarkInDB(BookmarkBaseInDB):
    pass
