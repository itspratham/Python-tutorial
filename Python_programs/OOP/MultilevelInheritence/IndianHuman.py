from OOP.MultilevelInheritence import HumanFile


class IndianHuman:

     def __init__(self,name,age,nl):
             HumanFile.Human.__init__(self,name,age)
             self.nl = nl

     def disply_human(self):
         print("Name is : {}".format(self.name))
         print("Age: {}".format(self.age))
         print("National Langaue {}".format(self.nl))


if __name__ =="__main__":
    h = IndianHuman('daksa',23,"hindi")
    h.disply_human()

