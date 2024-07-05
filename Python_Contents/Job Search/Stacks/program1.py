import math


class Stack:
    def __init__(self):
        self.lst = []

    def append(self, data):
        return self.lst.append(data)

    def pop(self):
        g = self.lst.pop()
        print(g, "is getting popped")
        return

    def print_stack(self):
        if len(self.lst) == 0:
            print("Empty")
            return None
        print(self.lst)
        return

    def delete_middle_number(self):
        if len(self.lst) <= 2:
            print("Cannot find middle number")
            return
        median = (1 + len(self.lst)) / 2
        self.lst.pop(math.floor(median - 1))
        return


l = Stack()
l.append(5)
l.append(6)
l.append(8)
l.append(7)
l.delete_middle_number()
l.print_stack()
