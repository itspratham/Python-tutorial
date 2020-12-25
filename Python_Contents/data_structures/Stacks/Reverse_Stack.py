class Stack:
    def __init__(self):
        self.l = []

    def append(self,item):
        return self.l.insert(0, item)

    def pop(self):
        return self.l.remove(self.l[0])

    def reverse(self):
        self.l = self.l[::-1]
        return self.l

    def print_list(self):
        return self.l


stack = Stack()
stack.append("A")
stack.append("B")
stack.append("C")
print(stack.print_list())
stack.reverse()
print(stack.print_list())
