#!/usr/bin/python3
"""
class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

sql_metadata = MetaData()
Base = declarative_base(metadata=sql_metadata)


class State(Base):
    """
    Class with `id` and `name` attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
