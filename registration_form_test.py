# registration_form_test.py
# Unit tests for registration_form.py
# Author: Jackie P, aka TheDataElemental. 1/24/22


import unittest
from registration_form import check_client_data


# Check for error upon entering already-present data (name, etc)
class TestNewData(unittest.TestCase):
	
	# Check for error upon entering already-taken name
	def test_taken_name(self):
		self.assertRaises\
			(ValueError, check_client_data, \
				'Taken Name', '', '')
				
	# Check for error upon entering already-taken phone number
	def test_taken_phone(self):
		self.assertRaises\
			(ValueError, check_client_data, \
				'', '1234567890', '')
				
	# Check for error upon entering already-taken email
	def test_taken_email(self):
		self.assertRaises\
			(ValueError, check_client_data, \
				'', '', 'TakenName@example.com')
		
