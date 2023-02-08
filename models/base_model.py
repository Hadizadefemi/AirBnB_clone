#!/usr/bin/python3
""" Module models/base_model.py
defines class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ inits with id, time created and updated time"""

        if len(kwargs) > 0:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)


        else:
            self.id = str(uuid.uuid4())
            created_time = datetime.now()
            self.created_at = created_time
            self.updated_at = datetime.now()

    def __str__(self):
        """ returns a string rep when instance of class is printed"""

        class_name = type(self).__name__
        instance_id = self.id
        instance_dict = self.__dict__.copy()

        return "[{}] ({}) {}".format(class_name, instance_id, instance_dict)

    def save(self):
        """ updates the updated_at attribute with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        """

        attr = self.__dict__.copy()
        attr["__class__"] = type(self).__name__
        attr["created_at"] = self.created_at.isoformat()
        attr["updated_at"] = self.updated_at.isoformat()
        return attr
