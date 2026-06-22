student_info = input("Student information: ")
comp_exercises = input("Exercises completed: ")


names = {}
exercises = {}

with open(student_info) as students:
    for line in students:
        line = line.strip()
        details = line.split(";")
        if details[0] == "id":
            continue
        names[details[0]] = [details[1], details[2]]


with open(comp_exercises) as exercise_db:
    for line in exercise_db:
        line = line.strip()
        details = line.split(";")
        if details[0] == "id":
            continue
        exercises[details[0]] = []
        for i in range(1, len(details)):
            exercises[details[0]].append(int(details[i]))


for key, value in names.items():
    print(f"{value[0]} {value[1]} {sum(exercises[key])}")