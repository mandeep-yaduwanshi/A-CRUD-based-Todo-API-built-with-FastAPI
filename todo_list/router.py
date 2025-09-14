from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db import get_db
from todo_list.dtos import UserSchema, TodoSchema
from todo_list.controller import (
    getUser, getTodosByUser, createUser, updateUser, deleteUser,
    getTodos, createTodo, updateTodo, deleteTodo
)

userRouter = APIRouter(prefix="/users")
todoRouter = APIRouter(prefix="/todos")

@userRouter.get("/")
def fetch_users(db: Session = Depends(get_db)):
    return getUser(db)

@userRouter.get("/{id}")
def fetch_user(id: int, db: Session = Depends(get_db)):
    return getUser(db, id)

@userRouter.get("/{id}/todos")
def fetch_user_todos(id: int, db: Session = Depends(get_db)):
    return getTodosByUser(id, db)

@userRouter.post("/")
def add_user(body: UserSchema, db: Session = Depends(get_db)):
    return createUser(body, db)

@userRouter.put("/{id}")
def modify_user(id: int, body: UserSchema, db: Session = Depends(get_db)):
    return updateUser(id, body, db)

@userRouter.delete("/{id}")
def remove_user(id: int, db: Session = Depends(get_db)):
    return deleteUser(id, db)

@todoRouter.get("/")
def fetch_todos(db: Session = Depends(get_db)):
    return getTodos(db)

@todoRouter.get("/{id}")
def fetch_todo(id: int, db: Session = Depends(get_db)):
    return getTodos(db, id)

@todoRouter.post("/user/{user_id}")
def add_todo(user_id: int, body: TodoSchema, db: Session = Depends(get_db)):
    return createTodo(body, user_id, db)

@todoRouter.put("/{id}")
def modify_todo(id: int, body: TodoSchema, db: Session = Depends(get_db)):
    return updateTodo(id, body, db)

@todoRouter.delete("/{id}")
def remove_todo(id: int, db: Session = Depends(get_db)):
    return deleteTodo(id, db)