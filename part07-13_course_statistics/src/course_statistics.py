import urllib.request
import json

def retrieve_all():
    result = []
    data = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = data.read()
    data = json.loads(data)
    for item in data:                               # data -> main list, item -> dicts
        if item["enabled"] == True:
            result.append((item["fullName"], item["name"], item["year"], sum(item["exercises"])))
    return result


def retrieve_course(course_name: str):
    result = {}
    data = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats")
    data = data.read()
    data = json.loads(data)

    result["weeks"] = len(data)
    max_students = None
    hours = 0
    exercises = 0
    for value in data.values():                 # value = subdictionaries
        if max_students == None or max_students < value["students"]:
            max_students = value["students"]
        hours += value["hour_total"]
        exercises += value["exercise_total"]
        avg_hours = hours // max_students
        avg_exec = exercises // max_students
    
    result["students"] = max_students
    result["hours"] = hours
    result["hours_average"] = avg_hours
    result["exercises"] = exercises
    result["exercises_average"] = avg_exec
    return result



if __name__ == "__main__":
    result = retrieve_course("docker2019")
    print(result)
    
