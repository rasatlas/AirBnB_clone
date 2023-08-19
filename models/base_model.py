#!/usr/bin/python3
import models
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

    def __init__(self, *args, **kwargs):
        """
        Constructor for a new BaseModel.
        Args:
            *args: unused.
            **kwargs (dict): Key/Value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            # Creates BaseModel from dictionary.
            # Converts datetime string values into datetime object values.
            # del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    datetime_obj = datetime.strptime(value, time_format)
                    setattr(self, key, datetime_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            # Instantiate id, created_at & update_at to default values
            # upon instantiation of an object.
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a human-readable string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the last updated time for an instance.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__ of
        the instance.
        """

        dict_format = {}
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_format["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_format[key] = value.strftime(time_format)
            else:
                dict_format[key] = value
        return dict_format
