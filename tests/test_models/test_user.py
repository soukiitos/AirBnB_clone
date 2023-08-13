#!/usr/bin/python3
'''Unittest for models/user.py'''
import os
import models
import unittest
from datetime import datetime
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    '''Testing instantiation'''
    def test_instantiation_no_args(self):
        self.assertEqual(User, type(User()))

    def test_instantiation_id(self):
        self.assertEqual(str, type(Use().id))


class TestUser_save(unittest.TestCase):
    '''Testing methods'''
    def test_save_args(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_update(self):
        usr = User()
        usr.save()
        idusr = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(idusr, f.read())


class TestUser_to_dict(unittest.TestCase):
    '''Testing to_dict method'''
    def test_to_dict(self):
        self.assertTrue(dict, type(User().to_dict()))


if __name__ == "__main__":
    unittest.main()
