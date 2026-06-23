# Write your solution here
def store_personal_data(person: tuple):
    person = list(person)
    with open("people.csv", "a") as people:
        person[1] = str(person[1])
        person[2] = str(person[2])
        line = ";".join(person)
        people.write(line + "\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))