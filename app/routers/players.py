from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import PlayerBase, PlayerDB, PlayerCreate, EventCreate
from ..database import players_crud, events_crud
from ..database.database import get_session


router = APIRouter(prefix='/players')

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_player(*, session: Session = Depends(get_session), player_in: PlayerCreate):
    player = players_crud.create_player(session, player_in)
    return player

@router.get("/", response_model=list[PlayerDB])
def get_players(*, session: Session = Depends(get_session)):
    players = players_crud.get_players(session)
    return players

@router.get("/{id}", response_model=PlayerDB)
def get_player(*, session: Session = Depends(get_session), id: int):
    return players_crud.get_player(session, id)

@router.delete("/{id}")
def delete_player(*, session: Session = Depends(get_session), id: int):
    return players_crud.delete_player(session, id)

@router.post("/{id}/events", status_code=status.HTTP_201_CREATED)
def create_event(*, session: Session = Depends(get_session), event_in: EventCreate):
    event = events_crud.create_event(session, event_in)
    return event