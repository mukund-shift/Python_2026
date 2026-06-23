# Write your solution here

def exp_solver(exp: str):
    if "+" in exp:
        index = exp.index("+")
        return int(exp[:index]) + int(exp[index:])
    else:
        index = exp.index("-")
        return int(exp[:index]) - int(exp[index + 1:])

def filter_solutions():
    open("correct.csv", "w").close()
    open("incorrect.csv", "w").close()
    with open("solutions.csv") as solutions:
        for line in solutions:
            line = line.strip()
            temp = line.split(";")
            print(temp)
            corr = exp_solver(temp[1])
            print(corr)
            if int(temp[2]) == corr:
                with open("correct.csv", "a") as correct:
                    correct.write(";".join(temp) + "\n")
                    print("Added to correct")
            else:
                with open("incorrect.csv", "a") as incorrect:
                    incorrect.write(";".join(temp) + "\n")
                    print("Added to incorrect")


if __name__ == "__main__":
    filter_solutions()