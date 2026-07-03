# Write your solution here

def change_case(orig_string: str):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    temp = list(orig_string)
    for i in range(len(temp)):
        if temp[i] in uppers:
            temp[i] = temp[i].lower()
        elif temp[i] in lowers:
            temp[i] = temp[i].upper()

    return "".join(temp)

def split_in_half(orig_string: str):
    length = len(orig_string)
    mid = length // 2
    return orig_string[:mid], orig_string[mid:]

def remove_special_characters(orig_string: str):
    non_special = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    temp = list(orig_string)
    for i in range(len(temp)):
        if temp[i] not in non_special:
            temp[i] = ""
    return "".join(temp)

if __name__ == "__main__":
    print(change_case("Well hello there!"))
    print(split_in_half("Well hello there!"))
    print(remove_special_characters("Well hello there!"))
