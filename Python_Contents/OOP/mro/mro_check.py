class F(object):
    pass

class E(object):
    pass

class D(object):
    pass

class C(D,F):
    pass

class B(D,E):
    pass

class A(B,C):
    pass


b = B()
print(C.__mro__)
print(D.mro())
print(E.mro())
print(E.__mro__)
print(B.__mro__)