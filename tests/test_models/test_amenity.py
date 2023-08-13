#!/usr/bin/python3
'''unittest for models/amenity.py'''
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    '''Testing instantiation'''
    def test_instantiation_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_public(self):
        self.assertEqual(str, type(Amenity().id))


class TestAmenity_save(unittest.TestCase):
    '''Testing unittest'''
    def test_save_args(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.save(None)

    def test_save_update(self):
        a = Amenity()
        a.save()
        ida = "Amenity." + a.id
        with open("file.json", "r") as f:
            self.assertIn(a, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    '''Testing to_dict method'''
    def test_to_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))


if __name__ == "__main__":
    unittest.main()
