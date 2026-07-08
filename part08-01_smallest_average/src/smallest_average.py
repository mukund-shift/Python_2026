# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    least_avg = None
    least_dict = None
    details = (person1, person2, person3)
    for person in details:
        temp = 0
        temp += person["result1"]
        temp += person["result2"]
        temp += person["result3"]
        avg = temp / 3
        if least_avg == None or avg < least_avg:
            least_avg = avg
            least_dict = person
    return least_dict

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))