#!/usr/bin/python3
"""State model with SQLAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''state model'''
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
