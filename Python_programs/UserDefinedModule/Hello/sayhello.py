import datetime
def greet():
    d = datetime.datetime.now()
    if int(d.hour) >= 5 and int(d.hour) < 12:
        print("Good Morning")
    elif int(d.hour) >= 12 and int(d.hour) < 14:
        print("Good Afternoon")
    else:
        print("Good evening")

