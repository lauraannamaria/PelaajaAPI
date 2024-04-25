from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class PlayerBase(SQLModel):
    name: str

class PlayerDB(PlayerBase, table=True):
    id: int = Field(default=None, primary_key=True)

class PlayerCreate(PlayerBase):
    pass

class EventBase(SQLModel):
    name: str

class EventDB(EventBase, table=True):
    id: int = Field(default=None, primary_key=True)