"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session, declarative_base, sessionmaker, relationship

# URI for connect
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

# add engine for async connect
engine = create_async_engine(PG_CONN_URI, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession))

async with async_session() as session:
    pass

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)

    posts = relationship("Post", back_populates="users")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String)
    body = Column(String)

    users = relationship("User", back_populates="posts")


Base.metadata.create.all(engine)
