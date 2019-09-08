class Point(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        st = "Point( {},{})".format(self.a, self.b)
        return st

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Point(a,b)

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return Point(a, b)

    def __ge__(self, other):
        if self.a > other.a and self.b > other.b:
            print("{} is greater".format(self))
        else:
            print("{} is greater".format(other))
    def __gt__(self, other):
        pass

    def __le__(self,other):
        pass

    def __eq__(self, other):
        pass

p1 = Point(10,20)
p2 = Point(30,60)
print(p1)
print(p2)

#(40,80)
p3 = p1 + p2
p4 = p1 * p2
p1 >= p2
print(p3)
print(p4)