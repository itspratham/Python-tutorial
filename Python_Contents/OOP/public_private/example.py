# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self, ggg):
        self.a = "GeeksforGeeks"
        self.__a = ggg

    def print_A(self):
        print(self.__a)


# Creating a derived class
class Derived(Base):
    def __init__(self, ggg):
        # Calling constructor of
        # Base class
        super().__init__(ggg)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base("444")
obj1.print_A()
obj1

#
# obj2  = Derived(obj1)
# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
