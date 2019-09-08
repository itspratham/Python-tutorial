from Exceptions import DateException

class MyDate(object):

    def __init__(self):
        self.dt = ""

    def getDate(self):
        try:
            self.dt = input("Enter the date ('dd/mm/yyyy')")
            splitdt = self.dt.split("/")
            d = int(splitdt[0])
            m = int(splitdt[1])
            y = int(splitdt[2])

        except DateException as e:
            if d >= 1 or d <=31:
                raise e("Invalid day")
            if m >= 1 or m <= 12:
                raise e("Invalid month")
            if y <=2018:
                raise e("Invlaid year")
            else:
                print(e)


    def putDate(self):
        print(self.dt)

mydate = MyDate()
mydate.getDate()
mydate.putDate()