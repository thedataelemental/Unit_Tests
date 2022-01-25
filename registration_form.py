# registration_form.py
# Mock registration form and client list for an online service.
# Author: Jackie P, aka TheDataElemental. 1/24/22


class Client:
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email


# Check if data from new entry is already present in list of clients
def check_client_data(name, phone, email):	
	global client_list
	
	for client in client_list:
		if client.name == name:
			raise ValueError("Name already taken.")
			
		elif client.phone == phone:
			raise ValueError("Phone number already taken.")
			
		elif client.email == email:
			raise ValueError("Email already taken.")


# Prompt user to enter new client data
def add_new_client():
	global client_list
	
	print("Enter user information. \n")

	name = input("Enter client name: ")
	phone = input("Enter client phone: ")
	email = input("Enter client email: ")
	
	check_client_data(name, phone, email)

	new_client = Client(name, phone, email)
	client_list.append(new_client)

	print("\nClient list:")
	for client in client_list:
		print("\nName:", client.name, \
			"\nPhone:", client.phone, \
			"\nEmail:", client.email)


first_client = Client('Taken Name', \
	'1234567890', \
	'TakenName@example.com')
	
client_list = [first_client]


# add_new_client()
