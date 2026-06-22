# Write your solution here
def longest(strings: list):
    max = len(strings[0])
    max_str = strings[0]
    for string in strings:
        if max < len(string):
            max = len(string)
            max_str = string
    return max_str
