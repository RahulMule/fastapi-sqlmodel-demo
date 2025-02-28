from typing import Optional,List
from sqlmodel import SQLModel,Field

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    genre: str
    platform : str
    release_year : int

class CreateGame(SQLModel):
    title: str
    genre: str
    platform : str
    release_year : int

class UpdateGame(SQLModel):
    title: str
    genre: str
    platform : str
    release_year : int
