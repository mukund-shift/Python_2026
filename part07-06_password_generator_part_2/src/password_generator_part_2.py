# Write your solution here
# Can actually use this for personal tasks(altho can use more rules to gen pass)
import random

def generate_strong_password(length: int, numbers: bool, special: bool):
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    specials = "!?=+-()#"
    result = ""
    chars = [letters]

    if numbers:
        chars.append(nums)
    if special:
        chars.append(specials)
    letter_char_present = False

    for i in range(length):
        choice = random.choice(chars)
        if choice == letters:
            letter_char_present = True
        char = choice[random.randint(0, len(choice) - 1)]
        result += char
    if not letter_char_present:
        result = list(result)
        result[random.randint(0, len(result) - 1)] = letters[random.randint(0, 25)]
        result = str(result)
    return result


if __name__ == "__main__":
    pw = generate_strong_password(2, False, False)
    print(pw)