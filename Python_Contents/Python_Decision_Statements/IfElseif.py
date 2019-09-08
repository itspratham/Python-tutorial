# Time 00 to 23
# Input the time from the user

tm = int(input("Enter the time:"))

if tm > 6 and tm < 12:
    print ("Good Morning")
elif tm > 12 and tm < 14:
    print ("Good Afternoon")
elif tm > 14 and tm < 20:
    print("Good Evening")
elif tm > 20 and tm < 23:
    print ("Good Night")
elif tm < 6:
    print ("Early Morning")
else:
    print ("Invalid time")
