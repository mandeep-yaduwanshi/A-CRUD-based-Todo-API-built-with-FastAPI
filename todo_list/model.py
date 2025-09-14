# model
# username, email, username, mobile,
# todd -
# title, description, peririty, start date, end date,
# user_
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from utils.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    mobile = Column(Integer, nullable=True) 

    todo = relationship("Todo", back_populates="user", cascade="all, delete-orphan")


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="todo", passive_deletes=True)