# Write your solution here
def oldest_person(people: list):
    oldest = people[0][1]
    oldest_pr = people[0][0]
    for i in range(len(people)):
        if people[i][1] < oldest:
            oldest = people[i][1]
            oldest_pr = people[i][0]
    return oldest_pr