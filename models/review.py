#!/usr/bin/python3
"""
It defines the Review class.
A module for Review class, it is a subclass of BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):

    """
    A subclass of BaseModel class which represent a review.

    Public class attributes:
        place_id (str): Place id
        user_id (str): User id
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
