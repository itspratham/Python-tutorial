class Stack(object):
    def __init__(self):
        self.elements=[]
        self.x = len(self.elements)

    def create_a_list_of_your_choice_size(self):
        self.size=int(input("enter the list size"))
        self.size=self.x

    def append(self,x):
        if len(self.elements)>self.size:
            self.elements.append(x)
            print("{} is appended to the list".format(x))
        else:
            print("Stack is overloaded")

    def pop(self):
        if self.size:
            print("Cannot pop")
        self.c=self.elements.pop()
        print("{} has popped off".format(self.c))

    def display(self):
        print("Your list is {}".format(self.elements) )


x= Stack()
x.create_a_list_of_your_choice_size()
x.append(6)
x.append(7)
x.pop()
x.display()