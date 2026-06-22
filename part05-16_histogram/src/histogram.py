# Write your solution here
def histogram(word: str):
    reps = {}
    for letter in word:
        if letter not in reps:
            reps[letter] = 0
        reps[letter] += 1
    for key, value in reps.items():
        print(f"{key} " + ("*" * reps[key]))

if __name__ == "__main__":
    histogram("abbba")