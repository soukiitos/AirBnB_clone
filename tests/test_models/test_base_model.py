#!/usr/bin/python3
"""
    Unittests for models/base_model.py.
"""

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):

    def test_two_created_at_attributes_of_two_different_instances(self):
        my_base1 = BaseModel()
        sleep(0.05)
        my_base2 = BaseModel()
        self.assertLess(my_base1.created_at, my_base2.created_at)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))


class TestBaseModelSave(unittest.TestCase):

    def test_save_updates_file(self) -> None:
        my_base = BaseModel()
        my_base.save()
        instance_id = f"BaseModel.{my_base.id}"
        with open("file.json", mode="r") as file:
            self.assertIn(instance_id, file.read())

    def test_one_save(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)


class TestBaseModelToDict(unittest.TestCase):

    def test_to_dict_by_adding_two_attributes(self):
        my_base = BaseModel()
        my_base.username = "Vanbasten"
        my_base.age = 34
        self.assertIn("username", my_base.to_dict())
        self.assertIn("age", my_base.to_dict())


if __name__ == "__main__":
    unittest.main()
