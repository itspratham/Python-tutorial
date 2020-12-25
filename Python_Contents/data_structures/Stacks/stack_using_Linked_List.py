class Node:
    def __init__(self,data):
        self.data = None
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            print("Inserted at the head")
            return self.head
        while self.head.next is not None:
            pass

