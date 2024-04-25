from fastapi import HTTPException
from .models import PlayerDB, PlayerBase, PlayerCreate
from sqlmodel import Session, select

#players = {
 #   0: {"id": 0, "name": "Laura"},
  #  1: {"id": 1, "name": "Emmi"},
   # 2: {"id": 2, "name": "Kikke"},
    #3: {"id": 3, "name": "Kati"}
#}

def create_player(session: Session, player_in: PlayerCreate):
    player_db = PlayerDB.model_validate(player_in)
    session.add(player_db)
    session.commit()
    session.refresh(player_db)
    return player_db


def get_players(session: Session):
    return session.exec(select(PlayerDB)).all()


def get_player(session: Session, id: int):
    player = session.get(PlayerDB, id)
    if not player:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return player


def delete_player(session: Session, id: int):
    player = session.get(PlayerDB, id)
    if not player:
        raise HTTPException(status_code=404, detail='ID not found')
    session.delete(player)
    session.commit()
    return {'message': f'Player with id {id} deleted'}