class MyNaturalNo(object):

    def __init__(self, limit):
        self.limit = limit
        self.n= 0

    def __iter__(self):
        #self.n=0
        return self

    def __next__(self):
        print("Next is called")
        if self.n == self.limit:
            raise StopIteration
        else:
            self.n+=1
            return self.n

mn= MyNaturalNo(5)
x=next(mn)
print(x)
y=x+10
print(y)


print("---------")
for i in mn:
    print(i)

    