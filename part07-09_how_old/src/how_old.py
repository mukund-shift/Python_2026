# Write your solution here
# Good idea for a mobile app

from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth = datetime(year, month, day)
millenium = datetime(1999, 12, 31)

if birth < millenium:
    result = millenium - birth
    print(f"You were {result.days} days old on the eve of the new millennium.")

else:
    print("You weren't born yet on the eve of the new millennium.")
