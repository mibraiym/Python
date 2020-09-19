import random
import string

def generate_pwd():
    name = input("Please enter your full name with no spaces: ").lower()
    if " " in name:
        print("Error! The name you have entered contains a space.")
    else:
        chars = random.sample(name, 3)
        digits = random.sample(string.digits,4)
        password ="".join(chars)+"".join(digits)
        print(password)

generate_pwd()
