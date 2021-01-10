from login_and_reg import *

print("Welcome to Oskar's Python Password Manager!")
choice = input("1: Login\n2: Register\n")
 
while choice not in ["1", "2"]:
	print("Invalid input")
	choice = input("1: Login\n2: Register\n")
 
if choice == "2":
	register()

is_logged_in = login()
 
