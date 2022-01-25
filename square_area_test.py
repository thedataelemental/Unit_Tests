# square_area_test.py
# Unit tests for square_area.py
# Author: Jackie P, aka TheDataElemental


import unittest
from square_area import get_square_area


class TestSquareArea(unittest.TestCase):
	
	# Test areas when length & width are >= 0
	def test_area(self):
		self.assertEqual(get_square_area(1, 1), 1)
		self.assertEqual(get_square_area(2, 4), 8)
	
	# Check for invalid values (negative numbers)
	def test_values(self):
		self.assertRaises(ValueError, get_square_area, -10, -2)
	
	# Check for invalid types
	def test_types(self):
		self.assertRaises(TypeError, get_square_area, 2+10j, 1+4j)
		self.assertRaises(TypeError, get_square_area, True, False)
		self.assertRaises(TypeError, get_square_area, "length", "width")
