from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from typing import List

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
    player_id: int = Field(default=None, foreign_key="PlayerDB.id")
    type: str = Field(max_length=50)
    detail: str= Field(default=None, max_length=100)
    timestamp: str = Field(default=None, max_length=20)


class EventCreate(EventBase):
    pass

events: List[EventDB] = Relationship(back_populates="player")

EventDB.player = Relationship(back_populates="events")