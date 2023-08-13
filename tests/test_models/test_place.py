#!/usr/bin/python3
'''unittest for models/place.py'''
import os
import models
import unittest
from datetime import datetime
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    '''Testing instantiation'''
    def test_instantiation_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_id_public(self):
        self.assertEqual(str, type(Place().id))

    def test_user_id_public(self):
        p = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(p))
        self.assertNotIn("user_id", p.__dict__)

    def test_city_id_public(self):
        p = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(p))
        self.assertNotIn("city_id", p.__dict__)

    def test_amenity_id_public(self):
        p = Place()
        self.assertEqual(str, type(Place.amenity_id))
        self.assertIn("amenity_id", dir(p))
        self.assertNotIn("amenity_id", p.__dict__)


class TestPlace_save(unittest.TestCase):
    '''Testing methods'''
    def test_save_args(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.save(None)

    def test_save_update(self):
        p = Place()
        p.save()
        idp = "Place." + p.id
        with open("file.json", "r") as f:
            self.assertIn(idp, f.read())


class TestPlace_to_dict(unittest.TestCase):
    '''Testinig to_dict methods'''
    def test_to_dict(self):
        self.assertTrue(dict, type(Place().to_dict()))


if __name__ == "__main__":
    unittest.main()
