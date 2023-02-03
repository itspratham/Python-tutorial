from Python_Contents.OOP.MultilevelInheritence import HumanFile


class IndianHuman(HumanFile.Human):

     def __init__(self,name,age,nl):
             super().__init__(name,age)
             self.nl = nl

     def disply_human(self):
         print("Name is : {}".format(self.name))
         print("Age: {}".format(self.age))
         print("National Language {}".format(self.nl))


if __name__ =="__main__":
    h = IndianHuman('daksa',23,"hindi")
    h.disply_human()
    print((IndianHuman.mro()))

