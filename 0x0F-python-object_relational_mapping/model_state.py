Quzeemoddusanwo
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x0F-python-object_relational_mapping/model_state.py
@Quzeemoddusanwo
Quzeemoddusanwo Add solutions to all tasks
 1 contributor
Executable File  23 lines (18 sloc)  573 Bytes
#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
