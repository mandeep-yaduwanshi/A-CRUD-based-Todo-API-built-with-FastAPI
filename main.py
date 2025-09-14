from fastapi import FastAPI
from utils.db import get_db
from sqlalchemy.orm import Session
from todo_list.router import todoRouter, userRouter
from utils.db import Base, engine


Base.metadata.create_all(engine)

server = FastAPI()
server.include_router(userRouter)
server.include_router(todoRouter)

@server.get("/")
def welcome():
    return "Code is working fine"