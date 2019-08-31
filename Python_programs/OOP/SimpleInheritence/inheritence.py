
class Human(object):
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):

    def __init__(self, name, age,total, avg):
        super().__init__(name,age)
        self.total =total
        self.avg = avg

    def display(self):
        print("Name:{}".format(self.name))
        print("Age:{}".format(self.age))
        print("Total:{}".format(self.total))
        print("Average:{}".format(self.avg))

s = Student("Jhon", 23,500,56)


s.display()


