#!/usr/bin/python3
"""
User class that inherits from BaseMode.
"""
from base_model import BaseModel


class User(BaseModel):
    """
    User class defintion.
    """
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
