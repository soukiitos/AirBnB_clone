#!/usr/bin/python3
'''unittest for models/state.py'''
import os
import models
import unittest
from datetime import datetime
from models.state import State


class TestState_instantiation(unittest.TestCase):
    '''Testing instantiation'''
    def test_instantiation_no_args(self):
        self.assertEqual(State, type(State()))


class TestState_save(unittest.TestCase):
    '''Testing methods'''
    def test_save_args(self):
        ste = State()
        with self.assertRaises(TypeError):
            ste.save(None)

    def test_save_update(self):
        ste = State()
        ste.save()
        idste = "State." + ste.id
        with open("file.json", "r") as f:
            self.assertIn(idste, f.read())


class TestState_to_dict(unittest.TestCase):
    '''Testing to_dict method'''
    def test_to_dict(self):
        self.assertTrue(dict, type(State().to_dict()))


if __name__ == "__main__":
    unittest.main()
