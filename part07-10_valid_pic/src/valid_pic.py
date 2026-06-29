# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    valid = True
    birth = pic[0:6]
    century_marker = pic[6]
    p_idf = pic[7:10]
    control_char = pic[10]

    try:
        if century_marker == "+":
            birthdate = datetime(int("18" + birth[4:]), int(birth[2:4]), int(birth[:2]))
        elif century_marker == "-":
            birthdate = datetime(int("19" + birth[4:]), int(birth[2:4]), int(birth[:2]))
        elif century_marker == "A":
            birthdate = datetime(int("20" + birth[4:]), int(birth[2:4]), int(birth[:2]))
        else:
            raise ValueError                        # Bad century marker
    
    except ValueError:
        return False                                # Filters bad markers & date

    temp = birth + p_idf
    temp = int(temp) % 31

    ref_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if ref_string[temp] != control_char:            # Filters control char
        return False
    return True

if __name__ == "__main__":
    result = is_it_valid("310823A9877")
    print(len("310923A9877"))
    print(result)
        