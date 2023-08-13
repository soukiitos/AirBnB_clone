#!/usr/bin/python3
'''unittest for models/city.py'''
import os
import models
import unittest
from datetime import datetime
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    '''Testing instantiation'''
    def test_instantiation_no_args(self):
        self.assertEqual(City, type(City()))

    def test_id_public(self):
        self.assertEqual(str, type(City().id))

    def test_city_id_public(self):
        c = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(c))
        self.assertNotIn("state_id", c.__dict__)


class TestCity_save(unittest.TestCase):
    '''Testing methods'''
    def test_save_args(self):
        c = City()
        with self.assertRaises(TypeError):
            c.save(None)

    def test_save_update(self):
        c = City()
        c.save()
        idc = "City." + c.id
        with open("file.json", "r") as f:
            self.assertIn(idc, f.read())


class TestCity_to_dict(unittest.TestCase):
    '''Testing to_dict method'''
    def test_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))


if __name__ == "__main__":
    unittest.main()
