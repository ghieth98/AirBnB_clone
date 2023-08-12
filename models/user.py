#!/usr/bin/python3
"""
It defines the User class.
A module for User class, it is a subclass of BaseModel.
"""

from models.base_model import BaseModel
import json


class User(BaseModel):

    """
    A subclass of BaseModel class which represent a user.

    Public class attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
