# Functions for the program's login and registration system

def login():
	print("\nSign in to Your Account")

	un = input("Enter Username: ")
	pw = input("Enter Password: ")

	try:
		user_file = open(un + ".txt", "r")
	except FileNotFoundError:
		print("User Does Not Exist")
		login()

	username, password = user_file.readlines()

	tries = 0
	while pw != password and tries < 4:
		print("Incorrect Password")
		pw = input("Enter Password: ")

		tries += 1

	if pw != password:
		print("Too Many Tries")
		return False

	print("Successful Login!")
	return True


def register():
	print("\nRegister Account")

	un = input("Select a Username: ")
	pw = input("Select a Password: ")
	
	try:
		user = open(un + ".txt", "r")
	except FileNotFoundError:
		while len(pw) < 6:
			print("Password Must Be at Least 6 Characters")
			pw = input("Select a Password: ")

		user_file = open(un + ".txt", "x")
		user_file.write(un + "\n" + pw)
		user_file.close()

		user_csv = open(un + ".csv", "x")
		user_csv.write("Name, Password")

		return

	print("Username Already Taken")
	register()

