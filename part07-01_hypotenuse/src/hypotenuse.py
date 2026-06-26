# Write your solution here

def hypotenuse(leg1: float, leg2: float):
    from math import sqrt
    hypt = sqrt(leg1**2 + leg2**2)
    return hypt

if __name__ == "__main__":
    print(hypotenuse(5,12))