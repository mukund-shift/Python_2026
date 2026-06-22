# Write your solution here
def dict_of_numbers():
    result = {}

    ones = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
            }

    tens = {
            1: "ten",
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
            }

    exceptions = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
    }
    
    for i in range(100):
        string = str(i)
        if len(string) == 1:
            result[i] = ones[i]
        elif string[0] == "1":
            result[i] = exceptions[i]
        else:
            msb = int(string[0])
            lsb = int(string[1])
            if lsb != 0:
                result[i] = f"{tens[msb]}-{ones[lsb]}"
            else:
                result[i] = tens[msb]
    return result

if __name__ == "__main__":
    b = dict_of_numbers()
    for key, value in b.items():
        print(f"{key} : {value}")

