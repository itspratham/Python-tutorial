class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next =new_node


    def print_list(self):
        currnode = self.head
        while currnode:
            print(currnode.data)
            currnode = currnode.next

    def delete_node(self,key):
        if self.head is None:
            print("No scope to delete the node")
            return
        curr_node = self.head
        if curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node.data and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        prev.next = curr_node.next
        curr_node = None

    def insert_at_an_index(self,position,data):
        newnode = Node(data)
        if self.head is None:
            print("List is empty and I can insert for you at 1st position")
            self.append(data)
            return
        curr_node = self.head
        if self.head.next is None and position == 1:
            self.head = newnode
            newnode.next = curr_node
            return
        prev = None
        count = 1

        while count!=position:
            prev = curr_node
            curr_node = curr_node.next
            count = count+1
        prev.next = newnode
        newnode.next = curr_node

    def rotate_left(self,position):
        if self.head is None and position<=0:
            return
        if self.head and position==1:
            return
        headd = self.head
        curr_node = self.head
        prev = None
        count = 1
        while count!=position:
            prev = curr_node
            curr_node = curr_node.next
            count = count + 1

        while curr_node:
            curr_node =curr_node.next

        curr_node.next = headd


l = LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.append("D")
l.append("E")
l.rotate_left(3)
l.print_list()
