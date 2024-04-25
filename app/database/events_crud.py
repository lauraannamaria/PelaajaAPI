from fastapi import HTTPException
from .models import EventBase, EventDB
from sqlmodel import Session, select

event_types = ["level_started", "level_completed", "item_collected"]


def get_events(session: Session):
    return session.exec(select(EventDB)).all()

def get_events_by_type(session: Session, event_types: str):
    query = select(EventDB).where(EventDB.type == event_types)
    return session.exec(query).all()