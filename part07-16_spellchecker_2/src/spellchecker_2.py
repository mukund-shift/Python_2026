# Write your solution here
from difflib import get_close_matches
text = input("Write text: ")

words = text.split(" ")
correct_words = []
suggestions = {}

with open("wordlist.txt") as reference:
    for line in reference:
        line = line.strip()
        correct_words.append(line)

correct_words = set(correct_words)


for i in range(len(words)):
    if words[i].lower() not in correct_words:
        words[i] = f"*{words[i]}*"
        suggestions[words[i][1:-1]] = get_close_matches(words[i][1:-1], correct_words)

print(" ".join(words))
print("suggestions:")
for key, value in suggestions.items():
    print(f"{key}: ", end = "")
    op_string = ""
    for item in value:
        op_string += f"{item}, "
    else:
        op_string = op_string[:-2]
    print(op_string)