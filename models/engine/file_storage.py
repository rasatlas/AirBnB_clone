#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
"""
Stores objects to file.
"""


class FileStorage:
    """
    File storage class implementation.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects, which contains all the objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the key-value pair in __objects.
        Class_name.id as key and obj as value.
        """
        class_name_id = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[class_name_id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __fille_path)
        """
        dictionary_obj = FileStorage.__objects
        for key, value in FileStorage.__objects.items():
            dictionary_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w') as jfile:
            json.dump(dictionary_obj, jfile, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised.)
        """
        try:
            with open(FileStorage.__file_path) as jfile:
                dict_obj = json.load(jfile)
                for obj_from_values in dict_obj.values():
                    class_name = obj_from_values["__class__"]
                    self.new(eval(class_name)(**obj_from_values))
        except FileNotFoundError:
            return
