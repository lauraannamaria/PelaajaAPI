from fastapi import HTTPException
from .models import EventBase, EventDB
from sqlmodel import Session, select

events = {
    0: {"id": 0, "type": "level_started", "detail": "level_1212_001", "timestamp": "2023-01-13 12:01:22", "player_id": 0},
    1: {"id": 1, "type": "level_started", "detail": "level_1212_001", "timestamp": "2023-01-13 12:01:22", "player_id": 1}
}


def create_event(session: Session, event_in: EventBase):
    eventdb = EventDB.model_validate(event_in)
    session.add(eventdb)
    session.commit()
    session.refresh(eventdb)
    return eventdb


def get_events(session: Session):
    return session.exec(select(EventDB)).all()


def get_event(id: int):
    if id not in events:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return events[id]


def delete_event(id: int):
    if id not in events:
        raise HTTPException(status_code=404, detail='ID not found')
    del events[id]
    return {'message': f'Event with id {id} deleted'}