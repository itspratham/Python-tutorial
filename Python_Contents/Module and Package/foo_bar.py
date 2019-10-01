class MyClass(object):

    """def __new__(cls):
        print("Im created")
        return cls"""

    def __init__(self):
        print("Im in __init__")

    def __add__(self, a):
        print("Hello You called the + operator")

    def __sub__(self, other):
        print("Hello You called the - operator")

    def __mul__(self, other):
        print("Hello You called the * operator")

s = MyClass()
r = MyClass()
# s+r
# s-r
# s*r
s
r
# print(10+10)
# print("Hello"+"World")
# print([1,2,3]+[4,5,6])
# print([1,2,3]*4)
# print("Hello"*4)

