# Write your solution here
book = {}
while True:
    action = input("command (1 search, 2 add, 3 quit): ")

    if action == "3":
        print("quitting...") 
        break

    name = input("name: ")

    if action == "2":
        if name not in book:
            book[name] = []
        book[name].append(input("number: "))
        print("ok!")
    else:
        if name in book:
            for i in range(len(book[name])):
                print(book[name][i])
        else:
            print("no number")