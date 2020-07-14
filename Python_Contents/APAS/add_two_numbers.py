class Node:
    def __init__(self,data):
       self.data = data
       self.next  = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        new_node =Node(data)
        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.next = None

    def print(self):
        if self.head is None:
            return
        cur_node = self.head
        data =""
        while cur_node:
            data = data +"".join(str(cur_node.data))
            cur_node = cur_node.next
        return int(data)

    def final_print(self):
        if self.head is None:
            return
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end="-->")
            cur_node = cur_node.next

    def reverse(self):
        if self.head is None:
            return
        prev = None
        cur_node = self.head
        while cur_node:
            nxt =cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        self.head = prev


ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(3)

ll.reverse()

c = ll.print()

ll = LinkedList()
ll.append(5)
ll.append(6)
ll.append(4)
ll.reverse()
d = ll.print()

total = c + d

ll = LinkedList()
while total>0:
    digit = total %10
    ll.append(digit)
    total = total // 10

ll.final_print()