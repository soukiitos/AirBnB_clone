#!/usr/bin/python3
"""The BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    '''initialize the BaseModel'''
    def __init__(self, *args, **kwargs):
        formt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, formt)
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    '''The str of the BaseModel'''
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """The update of the datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel"""
        dic = {}
        for key, value in self.__dict__.items():
            if (isinstance(value, datetime)):
                value = value.isoformat()
            dic[key] = value
        dic['__class__'] = self.__class__.__name__
        return dic
