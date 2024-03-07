#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Show a User.

    Attributes:
        email (str): The mail of the user.
        password (str): The pin of the user.
        first_name (str): The 1st name of the user.
        last_name (str): The 2nd name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
