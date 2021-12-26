class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="-->")
            current = current.next

    def prepend(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            prepend_node = Node(data)
            headd = self.head
            self.head = prepend_node
            prepend_node.next = headd

    def length(self):
        if self.head is None:
            return 0
        curnode = self.head
        count = 0
        while curnode:
            count = count + 1
            curnode = curnode.next
        return count

    def insert_at_the_particular_position(self, position, data):
        if self.head is None and position == 1:
            self.head = Node(data)
            return
        cur_node = self.head
        new_node = Node(data)
        count = 1
        while cur_node is not None:
            if position == count:
                next = cur_node.next
                cur_node.next = new_node
                new_node.next = next
                return
            cur_node = cur_node.next
            count = count + 1
        return "Cannot insert at that position"


a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = (input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end='')
print(a_llist.length())
# a_llist.display()
print(a_llist.length(), "length")
a_llist.insert_at_the_particular_position(3, "D")
print(a_llist.length())
a_llist.display()