class Stack(object):
    def __init__(self):
        self.items = []

    # method to check the stack is empty or not
    def isEmpty(self):
        return self.items == []

    # method for pushing an item
    def push(self, item):
        self.items.append(item)

    # method for popping an item
    def pop(self):
        return self.items.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.items[-1]

    # method to get the size
    def size(self):
        return len(self.items)

    # to view the entire stack
    def fullStack(self):
        return self.items

x=Stack()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
print('Current stack:', x.fullStack())
x.pop()
x.pop()
x.pop()
print('Current stack:', x.fullStack())