import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
try: 
    length = int(input("Type the length for the password: (default = 8) "))
except:
    length = 8
password = generate_password(length)
print(password)
