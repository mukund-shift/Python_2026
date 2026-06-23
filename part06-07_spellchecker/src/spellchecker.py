# write your solution here
text = input("Write text: ")

words = text.split(" ")
correct_words = []

with open("wordlist.txt") as reference:
    for line in reference:
        line = line.strip()
        correct_words.append(line)

correct_words = set(correct_words)


for i in range(len(words)):
    if words[i].lower() not in correct_words:
        words[i] = f"*{words[i]}*"

print(" ".join(words))