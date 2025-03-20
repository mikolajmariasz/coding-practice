import unittest

from main import *

class TestMyMethods(unittest.TestCase):
        def test_one(self):
            with self.assertRaises(ValueError):
                cal(',')
        def test_five(self):
            self.assertEqual(cal(''), 0)
        def test_two(self):
            self.assertEqual(cal('2'), 2)
        def test_three(self):
            self.assertEqual(cal('3,4'), 7)
        def test_four(self):
            self.assertEqual(cal('2100,10'), 2110)
        def test_six(self):
            self.assertEqual(cal('21,22,23,24,25'), 115)
        def test_seven(self):
            self.assertEqual(cal('0,0,0,0,0'), 0)
        def test_eight(self):
            self.assertEqual(cal('0,1,2\n1\n4'), 8)
        def test_nine(self):
            with self.assertRaises(ValueError):
                cal('\n1')
        def test_ten(self):
            with self.assertRaises(ValueError):
                cal('\n1\n')
