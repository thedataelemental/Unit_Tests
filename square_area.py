# square_area.py
# Find the area of a square given its length and width.
# Author: Jackie P, aka TheDataElemental


def get_square_area(square_length, square_width):
	
	# Check for errors
	for x in [square_length, square_width]:
		
		# Check for negative dimensions
		if x < 0:
			raise ValueError("Square's dimensions cannot be negative.")
			
		# Check for dimensions with incorrect types
		if type(x) != int:
			raise TypeError("Square's dimensions must be integers.")
	
	# Calculate and return area
	square_area = square_length * square_width
	return square_area
