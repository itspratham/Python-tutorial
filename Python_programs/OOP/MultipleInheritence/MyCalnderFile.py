from OOP.MultipleInheritence import MyDateFile
from OOP.MultipleInheritence import MyTimeFile

class MyCalendar(MyDateFile.MyDate, MyTimeFile.MyTime):
    def __init__(self,dd,mm,yyyy,hh,mi,ss):
        MyDateFile.MyDate.__init__(self, dd,mm,yyyy)
        MyTimeFile.MyTime.__init__(self, hh,mi, ss)

    def display(self):
        print("The Date and time is {}/{}/{} {}:{}:{}".format(self.date,self.month,self.year,self.hour, self.minute, self.second))



