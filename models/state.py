#!/usr/bin/python3
"""
It defines the State class.
A module for State class, it is a subclass of BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):

    """
    A subclass of BaseModel class which represent a state.

    Public class attributes:
        name (str): State name
    """

    name = ""
