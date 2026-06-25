# Write your solution here
def read_input(text, lb, ub):
    while True:
        try:
            number = int(input(text))
            if lb <= number <= ub:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lb} and {ub}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)