# write your solution here
def largest():
    with open("numbers.txt") as numbers:
        maxm = 0
        for number in numbers:
            if int(number) > maxm:
                maxm = int(number)
        return maxm