from OOP.MultilevelInheritence import IndianHuman

class LocalHuman:

    def __init__(self, name, age, nl, ll):
            IndianHuman.IndianHuman.__init__(self, name, age, nl)
            self.local_lang = ll

    def disply_human(self):
        print("Name is : {}".format(self.name))
        print("Age {}".format(self.age))
        print("National Langaue {}".format(self.nl))
        print("Local Langaue {}".format(self.local_lang))

