# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    operation = input("Function: ")

    if operation == "1":
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as diary:
            diary.write(f"{entry}\n")
        print("Diary saved")

    elif operation == "2":
        print("Entries:")
        with open("diary.txt") as diary:
            for line in diary:
                line = line.strip()
                print(line)

    elif operation == "0":
        print("Bye now!")
        break