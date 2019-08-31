class A:
    pass
    def who_am_i(self):
        print("I am a A")

class B(A):
    pass
    #def who_am_i(self):
    #    print("I am a B")

class C(A):
    pass
    #def who_am_i(self):
    #    print("I am a C")

class D(B,C):
    pass
    #def who_am_i(self):
    #    print("I am a D")

d1 = D()
d1.who_am_i()
print(D.__mro__)