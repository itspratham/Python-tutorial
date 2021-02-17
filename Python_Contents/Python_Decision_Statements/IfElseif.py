# Time 00 to 23
# Input the time from the user

tm = int(input("Enter the time:"))

if 6 < tm < 12:
    print("Good Morning")
elif 12 < tm < 14:
    print("Good Afternoon")
elif 14 < tm < 20:
    print("Good Evening")
elif 20 < tm < 23:
    print("Good Night")
elif tm < 6:
    print("Early Morning")
else:
    print("Invalid time")
