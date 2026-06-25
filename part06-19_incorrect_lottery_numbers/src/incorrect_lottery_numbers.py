# Write your solution here


def check(week_no: str, winning_nos: list):
    try:
        week_no = int(week_no)
        if len(winning_nos) != len(set(winning_nos)) or len(winning_nos) != 7:
            raise ValueError
        for number in winning_nos:
            number = int(number)
            if number < 1 or number > 39:
                raise ValueError
        return True
    except ValueError:
        return False
    

def filter_incorrect():
    with open("lottery_numbers.csv") as file:
        with open("correct_numbers.csv", "w") as correct:
            for line in file:
                line = line.strip()
                index = line.index(";")
                week_no = line[5:index]                     # 1
                winning_nos = line[index + 1:].split(",")   # 2
                if check(week_no, winning_nos):
                    correct.write(line + "\n")

if __name__ == "__main__":
    filter_incorrect()
