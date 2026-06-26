# Write your solution here

import string


def separate_characters(my_string: str):
    asci_set = set(string.ascii_letters)
    punc_set = set(string.punctuation)
    asci = ""
    punc = ""
    rest = ""
    for letter in my_string:
        if letter in asci_set:
            asci += letter
        elif letter in punc_set:
            punc += letter
        else:
            rest += letter
    return asci, punc, rest

if __name__ == "__main__":
    print(separate_characters("Hi!, I like doing exercises in Python."))