'''
Q2. Write a Python program that generates a password with the following conditions:
At least one uppercase letter.
At least one lowercase letter.
At least two numbers.
At least one special character (e.g., !@#$%&*).
The password should be exactly 16 characters long.
The password should contain no repeating characters.
The password should have a random order each time.
'''


import random
import string

def password_generator():
    
    uppercase = random.choice(string.ascii_uppercase)   
    lowercase = random.choice(string.ascii_lowercase)    
    digits = random.sample(string.digits, 2)             
    special = random.choice("!@#$%&*")                   

   
    all_chars = string.ascii_letters + string.digits + "!@#$%&*"
    remaining = random.sample(all_chars, 11)            
    
    password_list = [uppercase, lowercase] + digits + [special] + remaining
    random.shuffle(password_list)                       

   
    password = ''.join(password_list)
    return password



print("Generated Password:", password_generator())
