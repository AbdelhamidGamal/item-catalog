import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin

Base = declarative_base()


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    @staticmethod
    def get(user_email):
        user = session.query(User).filter_by(id=user_email)
        if not user:
            return None
        return user

    @staticmethod
    def create(id_, name, email):
        user = User(id=id, name=name, email=email)
        session.add(user)
        session.commit()


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
                "name": self.name,
                "id": self.id
        }


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    cat_id = Column(Integer, ForeignKey("category.id"))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
                "cat_id": self.cat_id,
                "id": self.id,
                "title": self.title,
                "description": self.description
        }


Base.metadata.create_all(engine)
