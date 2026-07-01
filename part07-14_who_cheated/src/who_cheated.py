# Write your solution here

def cheaters():
    cheaters = []
    start_info = {}
    with open("start_times.csv") as starts:
        for line in starts:
            line = line.strip()
            temp = line.split(";")
            subtemp = temp[1].split(":")
            temp[1] = subtemp
            start_info[temp[0]] = temp[1]

    with open("submissions.csv") as submits:
        for line in submits:
            line = line.strip()
            temp = line.split(";")
            subtemp = temp[3].split(":")
            temp[3] = subtemp
            time = subtemp
            hour_difference = int(time[0]) - int(start_info[temp[0]][0])
            minute_difference = int(time[1]) - int(start_info[temp[0]][1])
            cheated = False
            if hour_difference > 3:
                cheated = True
            elif hour_difference == 3 and minute_difference > 0:
                cheated = True
            if cheated and temp[0] not in cheaters:
                cheaters.append(temp[0])

    return cheaters
    

if __name__ == "__main__":
    cheaters = cheaters()
    print(len(cheaters))
