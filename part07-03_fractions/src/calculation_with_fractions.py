# Write your solution here

import fractions

def fractionate(amount: int):
    return [fractions.Fraction(1, amount)] * amount


if __name__ == "__main__":
    op = fractionate(10)
    for i in range(len(op)):
        print(op[i])
    print(op)