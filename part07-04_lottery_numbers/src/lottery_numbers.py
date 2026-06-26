# Write your solution here

import random


def lottery_numbers(amount: int, lower: int, upper: int):
    pool = list(range(lower, upper + 1))
    sample = random.sample(pool, amount)
    sample.sort()
    return sample

if __name__ ==  "__main__":
    example = lottery_numbers(25, 100, 999)
    print(example)