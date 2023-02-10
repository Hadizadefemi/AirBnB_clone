#!/usr/bin/python3
"""Module review
defines a class, Review which inherits from BaseModel
"""
from models.base_models import BaseModel


class Review(BaseModel):
    """Review of where the user wants to stay"""
    place_id = ""
    user_id = ""
    text = ""
