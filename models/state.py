#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Show a state.

    Attributes:
        call (str): The call of the state.
    """

    name = ""
