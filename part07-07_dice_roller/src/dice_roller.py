# Write your solution here
# Transitive die experiments (Very cool)
import random

def roll(dice: str):
    die = { "a" : [3, 3, 3, 3, 3, 6],
            "b" : [2, 2, 2, 5, 5, 5],
            "c" : [1, 4, 4, 4, 4, 4]}
    dice = dice.lower()
    return random.choice(die[dice])


def play(die1: str, die2: str, times: int):
    wins1 = 0
    wins2 = 0
    ties = 0
    for i in range(times):
        temp1 = roll(die1)
        temp2 = roll(die2)
        if temp1 > temp2:
            wins1 += 1
        elif temp2 > temp1:
            wins2 += 1
        else:
            ties += 1
    return wins1, wins2, ties
    

if __name__ == "__main__":
    
    result = play("A", "B", 1000)
    print(result)
    result = play("B", "C", 1000)
    print(result)
    result = play("A", "C", 1000)
    print(result)
    result = play("A", "A", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
    result = play("C", "C", 1000)
    print(result)