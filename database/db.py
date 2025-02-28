from sqlmodel import SQLModel, Field, Session, create_engine,select
from typing import Optional,List
import os
from dotenv import load_dotenv
load_dotenv()

#get connection string
database_url = os.getenv("database_url")
#create engine
engine = create_engine(database_url,echo=True)

def get_session():
    with Session(engine) as session:
        yield session

