# Write your solution here
def older_people(people: list, year: int):
    older = []
    for i in range(len(people)):
        #people is a list of lists where people[i][1] = age of i'th person
        if people[i][1] < year:
            older.append(people[i][0])
    return older
