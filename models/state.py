#!/usr/bin/python3
"""
State class that inherits from BaseModel.
"""
from base_model import  BaseModel


class State(BaseModel):
    """
    State class definition.
    """
    def __init__(self):
        self.name = ""
