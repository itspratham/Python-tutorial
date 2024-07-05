"""
from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.mainloop()

"""


# from tkinter import *
#
# window = Tk()
#
# window.title("Welcome to LikeGeeks app")
#
# lbl = Label(window, text="Hello")
#
# lbl.grid(column=1, row=1)
#
# window.mainloop()


# Python program showing the use of
# @property

class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Geeks()

mark.age = 19

print(mark.age)
