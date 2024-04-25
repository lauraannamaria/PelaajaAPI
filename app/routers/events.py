from fastapi import APIRouter, status, Depends
from ..database.models import EventBase, EventDB
from ..database import events_crud
from ..database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix='/events')

@router.get("/events", response_model=list[EventDB])
def get_events(session: Session = Depends(get_session)):
    return events_crud.get_events(session)


@router.get("/events/{type}", response_model=list[EventDB])
def get_events_by_type(session: Session = Depends(get_session)):
    return events_crud.get_events_by_type(session)
