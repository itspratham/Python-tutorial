class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = Node(data)
        return

    def print_linkedlist(self):
        if self.head is None:
            print("Empty linked list")
            return
        while self.head:
            print(self.head.data, end="==>")
            self.head = self.head.next

    def detect_Cycle(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return 1
        return 0


llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(10)
llist.head.next.next.next.next = llist.head

print(llist.detect_Cycle())
