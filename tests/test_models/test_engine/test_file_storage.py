#!/usr/bin/python3
"""unittests for models/engine/file_storage.py"""
import models
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Testing instantiation"""
    def test_FileStorage_instantiation_no_args(self):
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)


class TestFileStorage_method(unittest.TestCase):
    """Testing methods of the FileStorage class"""

    def test_new_method(self):
        """it test the 'new' method"""
        base = BaseModel()
        storage.new(base)
        base_key = f"BaseModel.{base.id}"
        self.assertIn(base_key, storage.all().keys())

    def test_reload_method(self):
        """it tests 'reload' method"""
        size1 = len(FileStorage.__objects)
        storage.reload()
        size2 = len(FileStorage.__objects)
        self.assertNotEqual(size1, size2)


if __name__ == "__main__":
    unittest.main()
