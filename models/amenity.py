#!/usr/bin/python3
"""Module amenity
Defines a class, amenity which inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenities users can choose from to offer at its place"""
    name = ""
