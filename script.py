import random
import string

def generate_password():
    charset = string.ascii_letters + string.digits + "@$%&"
    password = ''.join(random.choice(charset) for i in range(16))
    return password

print(generate_password())