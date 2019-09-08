class SimpleMath(object):
    num =10001
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def add(self):
        print ("{} + {} = {}".format(self.a, self.b, self.a+ self.b))

    def minus(self):
        print("{} - {} = {}".format(self.a, self.b, self.a - self.b))

    def multiply(self):
        print("{} x {} = {}".format(self.a, self.b, self.a * self.b))

    def divide(self):
        print("{} / {} = {}".format(self.a, self.b, self.a / self.b))
#===================================================================
p = 12122
q = 34343
sm = SimpleMath(p,q)
sm.add()
sm.minus()
sm.multiply()
sm.divide()
print (SimpleMath.num)
print(sm.num)
print("================================================")
p=10
q=2
sm1 = SimpleMath(p,q)
sm1.add()
sm1.minus()
sm1.multiply()
sm1.divide()

print(sm1.num)

