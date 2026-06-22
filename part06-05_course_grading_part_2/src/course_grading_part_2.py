# write your solution here

student_info = input("Student information: ")
comp_exercises = input("Exercises completed: ")
exam_points = input("Exam points: ")

if False:
    student_info = "students2.csv"
    comp_exercises = "exercises2.csv"
    exam_points = "exam_points2.csv"

names = {}
exercises = {}
points = {}

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


with open(exam_points) as exams:
    for line in exams:
        line = line.strip()
        details = line.split(";")
        if details[0] == "id":
            continue
        points[details[0]] = []
        for i in range(1, len(details)):
            points[details[0]].append(int(details[i]))


for key, value in names.items():
    total = 0
    
    total += sum(exercises[key]) // 4

    total += sum(points[key])
    
    grade = 0
    for i in range(15, 23, 3):
        if total >= i:
            grade += 1

    if total >= 24:
        grade += 1

    if total >= 28:
        grade += 1

    print(f"{value[0]} {value[1]} {grade}")