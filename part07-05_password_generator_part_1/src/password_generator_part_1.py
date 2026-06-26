# Write your solution here

import random

def generate_password(length: int):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        char = letters[random.randint(0, 25)]
        result += char
    return result