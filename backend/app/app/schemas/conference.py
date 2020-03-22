from typing import Optional

from pydantic import BaseModel


class ConferenceBase(BaseModel):
    name: Optional[str] = None


class ConferenceBaseInDB(ConferenceBase):
    id: int = None

    class Config:
        orm_mode = True


class Conference(ConferenceBaseInDB):
    pass


class ConferenceInDB(ConferenceBaseInDB):
    pass
