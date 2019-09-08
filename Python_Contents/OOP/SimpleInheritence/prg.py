class A(object):
    def __init__(self,a,b):
        self.a= a
        self.b=b


    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)


x=A(2,3)
x.add()
x.sub()