# Write your solution here
def factorials(n: int):
    factorials = {}
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        factorials[i] = temp
    return factorials