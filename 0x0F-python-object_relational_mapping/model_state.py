#!/usr/bin/python3
""" file that contains the class definition of a State and an instance Base"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())


class State(Base):
    """Class state table with id and name column"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
