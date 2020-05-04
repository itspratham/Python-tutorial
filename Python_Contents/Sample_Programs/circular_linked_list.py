class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next!=self.head:
                cur_node =cur_node.next
            cur_node.next = new_node
            new_node.next = self.head


    def prepend(self,data):
        new_node =Node(data)
        cur = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next

    def print_list(self):
        curnode = self.head
        while curnode:
            print(curnode.data)
            curnode = curnode.next
            if curnode==self.head:
                break



dl = CircularLinkedList()
dl.append("C")
dl.append("D")
dl.prepend("A")
dl.prepend("B")
dl.print_list()