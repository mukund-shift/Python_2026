# Write your solution here
def remove_smallest(numbers: list):
    min = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
    numbers.remove(min)