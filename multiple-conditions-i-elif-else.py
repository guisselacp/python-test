number = int(input("Please enter a number:"))

if number > 5:
    print(f"{number} is greater than 5")
elif number < 5:
    print(f"{number} is less than 5")
else:
    print(f"{number} is not greater than, or less than 5. Therefore, {number} must be equal to 5.")

#Challenge
day = 'Friday'

if day == 'Monday':
    print("Meeting at 9:00")
elif day == "Wednesday":
    print("Meeting at 2:00")
elif day =="Friday":
    print("Meeting at 4:00")
else:
    print("No meetings today")