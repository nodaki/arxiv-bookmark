from typing import Optional, List

from pydantic import BaseModel

from app.models.paper import Paper as DBPaper


# Shared properties
class UserBase(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    name: Optional[str] = None


class UserBaseInDB(UserBase):
    id: int = None
    bookmark_papers: Optional[List[DBPaper]] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


# Properties to receive via API on creation
class UserCreate(UserBaseInDB):
    email: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBaseInDB):
    password: Optional[str] = None


# Additional properties to return via API
class User(UserBaseInDB):
    bookmark_papers: Optional[list] = None


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str
