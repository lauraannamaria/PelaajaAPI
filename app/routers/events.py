from fastapi import APIRouter, status, Depends
from ..database.models import EventBase, EventDB
from ..database import events_crud
from ..database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix='/events')

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_event(*, session: Session = Depends(get_session), event_in: EventBase):
    return events_crud.create_event(session, event_in)

@router.get("/", response_model=list[EventDB])
def get_events(session: Session = Depends(get_session)):
    return events_crud.get_events(session)

@router.get("/{id}", response_model=EventDB)
def get_event(id: int):
    return events_crud.get_event(id)

@router.delete("/{id}")
def delete_event(id: int):
    return events_crud.delete_event(id)