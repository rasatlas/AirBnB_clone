#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
"""
BaseModel that defines all common attributes & methods for other classes.
"""


class BaseModel:
    """
    BaseModel definition & assignment of common default values to attributes
    to all instances of this class.
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a human-readable string representation of the instance.
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Saves the last updated time for an instance.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__ of
        the instance.
        """
        dict_format = {}
        dict_format["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_format[key] = value.isoformat()
            else:
                dict_format[key] = value
        return dict_format
