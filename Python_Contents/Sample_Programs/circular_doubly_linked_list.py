class Node:
    def __init__(self,data):
        self.data =data
        self.prev = None
        self.next = None

class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
            new_node.next = self.head
            return
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node
        new_node.next = self.head

    def print_list(self):
        curnode = self.head
        while curnode:
            print(curnode.data,end="-> ")
            curnode = curnode.next
            if curnode == self.head:
                break

    def prepend(self,data):
        if self.head is None:
            self.append(data)
            return
        new_node = Node(data)
        cur_node = self.head
        head_node = self.head
        self.head = new_node
        new_node.next = cur_node
        cur_node.prev = new_node
        new_node.prev = None

        while cur_node.next != head_node:
            cur_node = cur_node.next

        cur_node.next = new_node

    def rotation_of_linked_list(self,pos):
        if self.head.next == self.head:
            return
        cur_node = self.head
        head_node = self.head
        count = 0
        while count<pos:
            prev =cur_node
            cur_node = cur_node.next
            count = count + 1
        self.head = cur_node
        cur_node.prev = None
        prev.next = cur_node
        while cur_node.next != head_node:
            cur_node = cur_node.next
        cur_node.next = head_node
        head_node.prev = cur_node

dl = Circular_Doubly_Linked_List()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.append(5)
dl.append(6)
dl.rotation_of_linked_list(2)
dl.print_list()
