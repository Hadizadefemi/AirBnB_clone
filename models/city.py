#!/usr/bin/python3
"""Module city
defines a class, city which inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """city to look for"""
    state_id = ""
    name = ""
