#!/usr/bin/python3
"""
It defines the City class.
A module for City class, it is a subclass of BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):

    """
    A subclass of BaseModel class which represent a city.

    Public class attributes:
        state_id (str): The state id
        name (str): The city name
    """

    state_id = ""
    name = ""
