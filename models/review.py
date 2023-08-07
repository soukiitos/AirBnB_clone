#!/usr/bin/python3
'''The class Review that inherit from BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
