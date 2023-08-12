#!/usr/bin/python3
"""
It defines the Place class.
A module for Place class, it is a subclass of BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):

    """
    A subclass of BaseModel class which represent a place.

     Public class attributes:
        city_id (str): City id
        user_id (str): User id
        name (str): Place name
        description (str): A description of the place
        number_rooms (int): A number of rooms of the place
        number_bathrooms (int): A number of bathrooms of the place
        max_guest (int): The maximum number of guests of the place
        price_by_night (int): The price by night of the place
        latitude (float): A latitude of the place
        longitude (float): A longitude of the place
        amenity_ids (list): A list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
