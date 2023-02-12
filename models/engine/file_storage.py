#!/usr/bin/python3
""" Module file_storage
defines class, FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """ serializes instances to a JSON file, vice versa"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""

        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""

        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        from base_model import BaseModel
        from user import User
        from place import Place
        from city import City
        from amenity import Amenity
        from state import State
        from review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
