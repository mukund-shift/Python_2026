# Write your solution here
def invert(dictionary: dict):
    copy = {}
    for key, value in dictionary.items():
        copy[value] = key
    dictionary.clear()
    for key, value in copy.items():
        dictionary[key] = value
