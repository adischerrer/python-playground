import unittest
from math import pi

from m20_circles import circle_area


class TestCircleArea(unittest.TestCase):
    def test_area_positive(self):
        # Test areas when radius > 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_area_zero(self):
        # Test areas when radius = 0
        self.assertAlmostEqual(circle_area(0), 0)

    def test_negative_argument(self):
        # Ensure an exception is raised for negative arguments
        self.assertRaises(ValueError, circle_area, -2)

    def test_bad_argument_type(self):
        # Ensure an exception is raised for bad argument types
        self.assertRaises(TypeError, circle_area, 'text')
        self.assertRaises(TypeError, circle_area, True)
