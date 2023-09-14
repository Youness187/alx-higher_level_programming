#!/usr/bin/python3
"""
Models State
"""
from sqlalchemy import Column, Integer, String
from relationship_city import Base
from sqlalchemy.orm import relationship


class State(Base):
    """class of state Database"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
