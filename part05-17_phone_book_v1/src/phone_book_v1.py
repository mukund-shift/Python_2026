# Write your solution here
book = {}
while True:
    action = input("command (1 search, 2 add, 3 quit): ")

    if action == "3":
        print("quitting...") 
        break

    name = input("name: ")

    if action == "2":
        book[name] = input("number: ")
        print("ok!")
    else:
        if name in book:
            print(book[name])
        else:
            print("no number")