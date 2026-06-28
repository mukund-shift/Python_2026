# Write your solution here
import random

all_words = set()

with open("words.txt") as words:
    for line in words:
        line = line.strip()
        all_words.add(line)

def words(n: int, beginning: str):
    matches = []
    for word in all_words:
        if word.startswith(beginning):
            matches.append(word)
    if len(matches) < n:
        raise ValueError
    return random.sample(matches, n)


if __name__ == "__main__":
    word_list = words(4, "bl")
    print(word_list)