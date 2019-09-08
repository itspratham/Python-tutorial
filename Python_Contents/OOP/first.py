class Foo(object):

    def __init__(self, name):
        self.name = name

    def tell_hello(self):
        print("Hello", self.name)


names = ["Albert", "Bill", "Charls", "David",1]
list_of_objs = []
for name in names:
    obj = Foo(name)
    list_of_objs.append(obj)



for obj in list_of_objs:
   obj.tell_hello()