# Write your solution here
# Write your solution here

def start_time_analyzer():
    start_info = {}
    with open("start_times.csv") as starts:
        for line in starts:
            line = line.strip()
            temp = line.split(";")
            subtemp = temp[1].split(":")
            temp[1] = subtemp
            start_info[temp[0]] = temp[1]
    return start_info

def line_to_list(line:str):                         # only for submit_info
    line = line.strip()
    temp = line.split(";")
    time = temp[3].split(":")
    return temp[:3], time

def cheat_filter(end: list, start: list):
    hour_difference = int(end[0]) - int(start[0])
    minute_difference = int(end[1]) - int(start[1])
    cheated = False
    if hour_difference > 3:
        cheated = True
    elif hour_difference == 3 and minute_difference > 0:
        cheated = True
    return cheated

def final_points():
    start_info = start_time_analyzer()                      # Builds start_info: {name: time}
#correct upto here
    submit_info = {}
    with open("submissions.csv") as submits:
        for line in submits:
            temp, time = line_to_list(line)                 # temp = ["name", "task", "pts"], time = ["hr": "min"]       

            if cheat_filter(time, start_info[temp[0]]):
                continue
                
            if temp[0] not in submit_info:
                submit_info[temp[0]] = {}
            if temp[1] not in submit_info[temp[0]]:
                submit_info[temp[0]][temp[1]] = temp[2]
                                                                    # evaluates to point of course: temp[1]
            else:
                points = int(submit_info[temp[0]][temp[1]]) 
                if int(temp[2]) > points:                                # temp[2] == current line points
                    submit_info[temp[0]][temp[1]] = temp[2]
                
    result = {}
    for key, value in submit_info.items():
        result[key] = 0
        for subvalue in value.values():
            result[key] += int(subvalue)

    return result
                


if __name__ == "__main__":
    final = final_points()
    print(final)