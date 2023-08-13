#!/usr/bin/python3
'''unittest for models/review.py'''
import os
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    '''Testing instantiation'''
    def test_instantiation_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_id_public(self):
        self.assertEqual(str, type(Review().id))


class TestReview_save(unittest.TestCase):
    '''Testing methods'''
    def test_save_args(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.save(None)

    def test_save_update(self):
        r = Review()
        r.save()
        idr = "Review." + r.id
        with open("file.json", "r") as f:
            self.assertIn(idr, f.read())


class TestReview_to_dict(unittest.TestCase):
    '''Testing to_dict methods'''
    def test_to_dict(self):
        self.assertTrue(dict, typ(Review().to_dict()))


if __name__ == "__main__":
    unittest.main()
