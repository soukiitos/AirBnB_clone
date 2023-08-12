#!/usr/bin/python3
'''Define unittests for models/engine/file_storage.py'''
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class TestFileStorage_instantiation(unittest.TestCase):

    '''Testing instantiation'''
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    '''Testing instantiation'''
    def test_FileStorage_instantiation_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    '''Testing instantiation'''
    def test_FileStorage_file_path_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    '''Testing instantiation'''
    def test_FileStorage_objects_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    '''Testing instantiation'''
    def test_FileStorage_initialize(self):
        self.assertEqual(type(models.storage), FileStorage)


'''Testing methods of the FileStorage class'''


class TestFileStorage_method(unittest.TestCase):

    '''Define the setUp'''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    '''Define the tearDown'''
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    '''Define all tests'''
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    '''Define all tests with args'''
    def test_all_args(self):
        with self.asseertRaises(TypeError):
            models.storage.all(None)

    '''Define new tests'''
    def test_new(self):
        cls_instances = {
                BaseModel: None,
                User: None,
                State: None,
                Place: None,
                City: None,
                Amenity: None,
                Review: None
                }
        for cls in cls_instances.keys():
            instance = cls()
            cls_instances[cls] = instance
            models.storage.new(instance)
        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            for cls, instance in cls_instances.items():
                if instance is not None:
                    instance_id = instance.id
                    self.assertIn(f"{cls.__name__}.{instance_id}", save_text)

    '''Define new tests with args'''
    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    '''Define new tests without args'''
    def test_new_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    '''Define the save tests'''
    def test_save(self):
        cls_instances = {
                BaseModel: None,
                User: None,
                State: None,
                Place: None,
                City: None,
                Amenity: None,
                Review: None
                }
        for cls in cls_instances.keys():
            instance = cls()
            cls_instances[cls] = instance
            models.storage.new(instance)
        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            for cls, instance in cls_instances.items():
                if instance is not None:
                    instance_id = instance.id
                    self.assertIn(f"{cls.__name__}.{instance_id}", save_text)

    '''Define the save tests with args'''
    def test_save_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    '''Define the reload tests'''
    def test_reload(self):
        cls_instances = {
                BaseModel: None,
                User: None,
                State: None,
                Place: None,
                City: None,
                Amenity: None,
                Review: None
                }
        for cls in cls_instances.keys():
            instance = cls()
            cls_instances[cls] = instance
            models.storage.new(instance)
        models.storage.save()
        models.storage.reload()
        objs = models.storage.all()
        for cls, instance in cls_instances.items():
            if instance is not None:
                self.assertIn(f"{cls.__name__}.instance.id}", objs)

    '''Define the no files reload'''
    def test_reload_no_files(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    '''Define the reload tests with args'''
    def test_reload_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
