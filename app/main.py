from fastapi import FastAPI,HTTPException, Depends
from sqlmodel import SQLModel,Session,select
from database.db import engine,get_session
from models.game import CreateGame,Game
from typing import List
app = FastAPI()

SQLModel.metadata.create_all(engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

#add new game
@app.post("/games", response_model=Game)
async def addgame(game:CreateGame,db : Session = Depends(get_session)):
    new_game = Game(**game.model_dump())
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game

@app.get("/games", response_model=List[Game])
async def getallgames(db : Session = Depends(get_session)):
    games = db.exec(select(Game)).all()
    return games

@app.get("/games/{gameid}", response_model=Game)
async def getallgames(gameid:int,db : Session = Depends(get_session)):
    game = db.get(Game,gameid)
    if game:
        return game
    else:
        raise HTTPException(status_code=404,detail="Game not available")
@app.delete("/games/{gameid}",response_model=dict)
async def removegame(gameid : int , db : Session = Depends(get_session)):
    game = db.get(Game,gameid)
    if game:
        db.delete(game)
        db.commit()
        return {"message": "Game deleted successfully"}
    else:
        raise HTTPException(status_code=404,detail="Game not available")