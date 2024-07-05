# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_Data = Node(data)
        if self.head is None:
            self.head = Node(data)
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_Data
        return

    def print_Data(self):
        if self.head is None:
            return "Empty List"
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        return

    def Swap_Nodes_in_Pairs(self):
        if self.head is None:
            return []
        cur_node = self.head
        while cur_node and cur_node.next:
            first_node = cur_node
            second_node = cur_node.next
            second_node.next = first_node
            first_node.next = second_node
        return

    def __del__(self):
        print("i am automatically destroyed")
        return

def func():
    ll = LinkedList()
    ll.append("A")
    ll.append("B")
    ll.append("C")
    ll.append("D")
    ll.print_Data()
    ll.Swap_Nodes_in_Pairs()
    ll.print_Data()
    return
func()