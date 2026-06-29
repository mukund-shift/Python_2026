# Write your solution here
import datetime as dt

screen_times = {}

file_name = input("Filename: ")
start_date = dt.datetime.strptime(input("Starting date: "), "%d.%m.%Y")
one_day = dt.timedelta(days = 1)
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

temp_date = start_date
total = 0
for i in range(days):               # Dictionary population + total & avg calc
    input_string = dt.datetime.strftime(temp_date, "Screen time %d.%m.%Y: ")
    screentime_str = input(input_string)
    screen_time = screentime_str.split(" ")
    screen_times[temp_date] = "/".join(screen_time)
    temp_date += one_day

    for item in screen_time:
        total += int(item)

temp_date -= one_day                # Adjusting for one extra day added in loop
average = total / days

with open(file_name, "w") as file:
    start = dt.datetime.strftime(start_date, "%d.%m.%Y")
    end = dt.datetime.strftime(temp_date, "%d.%m.%Y")
    file.write(f"Time period: {start}-{end}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {average}\n")

    for key, item in screen_times.items():
        temp = dt.datetime.strftime(key, "%d.%m.%Y")
        file.write(f"{temp}: {item}\n")
