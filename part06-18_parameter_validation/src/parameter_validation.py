# Write your solution here

def check(name: str, age: int):
    if name == "" or len(name) > 40:
        raise ValueError("Enter proper values stupid")
    name = name.split(" ")
    if len(name) < 2:
        raise ValueError("Enter proper values stupid")
    if age < 0 or age > 150:
        raise ValueError("Enter proper values stupid")
    
def new_person(name: str, age: int):
    check(name, age)
    return (name, age)