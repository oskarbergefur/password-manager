import random

def generate_password():
	chars = "!\”#€%&/()=?¨+^~1234567890qwertyuiopåasdfghjklöäzxcvbnm,.-;:_*<>QWERTYUIOPÅASDFGHJKLÖÄZXCVBNM"
	
	password = ""
	for i in range(10):
		j = random.randrange(len(chars))
		password += chars[j]

	return password

print(generate_password())

