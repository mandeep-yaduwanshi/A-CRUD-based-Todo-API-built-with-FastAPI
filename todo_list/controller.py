from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from todo_list.dtos import UserSchema, TodoSchema
from todo_list.model import User, Todo


def getUser(db: Session, id: int = None):
    if id:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"Error": "User not found"})
        return {
            "user": user,
            # "todos": user.todo
        }
    return db.query(User).all()

def getTodosByUser( id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"Error": "User not found"})
    return {
        "User": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "mobile": user.mobile
        },
        "Todos": user.todo
    }

def createUser(body: UserSchema, db: Session):
    existing = db.query(User).filter(User.email == body.email).first()
    if existing:
        return {"Status": "Already Exists", "User": existing}
    newUser = User(**body.model_dump())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return {"Status": "Done", "NewUser": newUser}


def updateUser(id: int, body: UserSchema, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(404, detail={"Error": "User not found"})
    data = body.model_dump()
    for k, v in data.items():
        setattr(user, k, v)
    db.commit()
    db.refresh(user)
    return {"Status": "User updated successfully", "UpdatedUser": user}


def deleteUser(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(404, detail={"Error": "User not found"})
    db.delete(user)
    db.commit()
    return {"Message": "User deleted", "DeletedUser": user}


def getTodos(db: Session, id: int = None):
    if id:
        todo = db.query(Todo).filter(Todo.id == id).first()
        if not todo:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"Error": "Todo not found"})
        return todo
    return db.query(Todo).all()


def createTodo(body: TodoSchema, user_id: int, db: Session):
    newTodo = Todo(**body.model_dump(), user_id=user_id)
    db.add(newTodo)
    db.commit()
    db.refresh(newTodo)
    return {"Status": "Done", "NewTodo": newTodo}


def updateTodo(id: int, body: TodoSchema, db: Session):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(404, detail={"Error": "Todo not found"})
    data = body.model_dump()
    for k, v in data.items():
        setattr(todo, k, v)
    db.commit()
    db.refresh(todo)
    return {"Status": "Todo updated successfully", "UpdatedTodo": todo}


def deleteTodo(id: int, db: Session):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(404, detail={"Error": "Todo not found"})
    db.delete(todo)
    db.commit()
    return {"Message": "Todo deleted", "DeletedTodo": todo}