#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): Show City id.
        user_id (str): Show User id.
        name (str): Give the name of the place.
        description (str): Describe of the place.
        number_rooms (int): The count of place of the room.
        number_bathrooms (int): The count of washrooms of the place.
        max_guest (int): The max namder of visitor of the place.
        price_by_night (int): The cost by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
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
