#!/usr/bin/python3
""" Module user
a class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines attribute for a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
