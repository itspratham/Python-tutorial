# Union and Intersection of two Linked Lists


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         #self.last = None
#
#     def append(self, data):
#         if self.head is None:
#             self.head = Node(data)
#             return
#         head_node = self.head
#         new_node = Node(data)
#         while head_node.next:
#             head_node = head_node.next
#         head_node.next = new_node
#
#
#     def print_list(self):
#         currnode = self.head
#         while currnode:
#             print(currnode.data)
#             currnode = currnode.next
#
# ll = LinkedList()
#
# ll.append("A")
# ll.append("B")
# ll.append("C")
# ll.append("D")
# ll.print_list()



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
        newnode = Node(data)
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = newnode

    def print_list(self):
        curnode = self.head
        while curnode:
            print(curnode.data,"-->", end="")
            curnode = curnode.next

    # def union_of_two_list(self, l1,l2):
    #     head_node1 = self.head
    #     head_node2 = se

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.print_list()
