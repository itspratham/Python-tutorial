import datetime


def greet():
    d = datetime.datetime.now()
    if 5 <= int(d.hour) < 12:
        print("Good Morning")
    elif 12 <= int(d.hour) < 14:
        print("Good Afternoon")
    else:
        print("Good evening")
