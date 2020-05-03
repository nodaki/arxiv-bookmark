from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: Optional[str] = None


class AuthorBaseInDB(AuthorBase):
    id: int = None

    class Config:
        orm_mode = True


class AuthorCreate(AuthorBaseInDB):
    pass


class Author(AuthorBaseInDB):
    pass
