# Write your solution here
def add_student(database: dict, name: str):
    database[name] = {}


def print_student(database: dict, name: str):
    if name not in database:
        print(f"{name}: no such person in the database")
    else:
        print(name + ":")
        if database[name] == {}:
            print(" no completed courses")
        else:
            avg = 0
            print(f" {len(database[name])} completed courses:")
            for key, value in database[name].items():
                print("  " + key, value)
                avg += value
            avg /= len(database[name])
            print(f" average grade {avg}")
                


def add_course(database: dict, name: str, data: tuple):
    if data[1] != 0:
        if data[0] not in database[name] or database[name][data[0]] < data[1]:
            database[name][data[0]] = data[1]

def summary(database: dict):
    max_avg = 0
    max_avg_name = ""
    most_courses = 0
    most_courses_name = ""
    for i in database:
        avg = 0
        courses = len(database[i])
        if courses > most_courses:
            most_courses = courses
            most_courses_name = i
        for j in database[i]:
            avg += database[i][j]
        avg /= len(database[i])
        if avg > max_avg:
            max_avg = avg
            max_avg_name = i
    
    print(f"students {len(database)}")
    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {max_avg} {max_avg_name}")

    
