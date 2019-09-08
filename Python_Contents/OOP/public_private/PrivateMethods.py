class Hello(object):

    def __init__(self):
        self.__a ="10"

    def __str__(self):
        return (str(self.__a))

    def __dis(self):
        print("Good Morning")
        print(self.__a)

h = Hello()
print(h)
#h.dis()
#print(h.a)