"""

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())
"""


# from decorator.Decorators_1 import my_decorator
#
# @my_decorator
# def fun1():
#     print("hi")
#
# fun1()


# Python program to
# demonstrate private members

# # Creating a Base class
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"
#
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
#
#
# # Driver code
# obj1 = Base()
# print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

# From = "Bangalore"
# print(len(From))


# def a_func(n):
#     count = 1
#     a_list = []
#     while count <= n:
#         a_list.append(count)
#         count = count + 2
#     return a_list
# print(a_func(10))

# a = []
#
# for i in range(10):
#     a.append(i)
# print(a)

# a = 10
#
#
# class A:
#     a = 100
#
#     def sum(self):
#         return a
#
#
# print(A().sum())
# class A:
#     a = 1
#     b = 2
#
#
# class B:
#     a = 10
#
#     def sum(self):
#         return self.a + self.b
#
#
# class C(B, A):
#     pass
#
#
# print(C().sum())


# def decorator(func):
#     def wrapper()
