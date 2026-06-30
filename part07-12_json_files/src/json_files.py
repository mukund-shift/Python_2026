# Write your solution here
# json is very simple, just a list of dictionaries containing attributes
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        data = json.loads(data)
    for item in data:
        # item == dicts
        print(item["name"], end = " ")
        print(f"{item["age"]} years", end = " (")
        sublist = item["hobbies"]
        for i in range(len(sublist)):
            print(sublist[i], end = "")
            if i <= len(sublist) - 2:
                print(", ", end = "")
        else:
            print(")")

if __name__ == "__main__":
    print_persons("file4.json")
