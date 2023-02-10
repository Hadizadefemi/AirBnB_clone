#!/usr/bin/python3
"""Module state
defines class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """state of the user"""
    name = ""
