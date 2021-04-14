import unittest

from modules.calculator import *

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.num_1 = 10
        self.num_2 = 5

    def test_add(self):
        self.assertEqual(15, add(self.num_1, self.num_2))

    def test_subtract(self):
        self.assertEqual(5, subtract(self.num_1, self.num_2))

    def test_multiply(self):
        self.assertEqual(50, multiply(self.num_1, self.num_2))

    def test_divide(self):
        self.assertEqual(2, divide(self.num_1, self.num_2))