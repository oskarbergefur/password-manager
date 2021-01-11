# Functions for generating and saving a new password

import random


def generate_pw():
    chars = "!\”#€%&/()=?¨+^~1234567890qwertyuiopåasdfghjklöäzxcvbnm,.-;:_*<>QWERTYUIOPÅASDFGHJKLÖÄZXCVBNM"

    pw = ""
    for i in range(10):
        j = random.randrange(len(chars))
        pw += chars[j]

    return pw


def new_pw(un, name=None):
    print("\nGenerate New Password")

    if not name:
        name = input("Enter Name: ")
    
    pw = generate_pw()
    print("Your Password is {}.".format(pw))

    choice = input("1: Save\n2: Generate New Password\n")
    while choice not in ["1", "2"]:
        print("Invalid input")
        choice = input("1: Save\n2: Generate New Password\n")

    if choice == "2":
        return new_pw(un, name)

    user_csv = open(un + ".csv", "a")
    user_csv.write("\n{}, {}".format(name, pw))

    print("Password Saved!")

