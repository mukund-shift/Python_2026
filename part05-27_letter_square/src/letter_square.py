# Write your solution here
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layers = int(input("Layers:"))
index = layers - 1
final = []


def box_printer(index):
    length = (2 * layers) - 2
    
    for i in range(length + 1):
        ctr = 0
        static_ctr = min(i, abs(i - length))
        for j in range(length + 1):

            if j > length - static_ctr:
                ctr -= 1

            print(letters[index - ctr], end = "")

            if ctr < min(i, abs(i - (length))) and j < index:
                ctr += 1

        print()

box_printer(index)