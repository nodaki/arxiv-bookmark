from typing import Optional

from pydantic import BaseModel


class TagBase(BaseModel):
    name: Optional[str] = None


class TagBaseInDB(TagBase):
    id: int = None

    class Config:
        orm_mode = True


class Tag(TagBase):
    pass
