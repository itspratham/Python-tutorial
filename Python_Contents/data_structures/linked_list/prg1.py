# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
#
#     def append(self, data):
#         if self.last_node is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
#
#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end = ' ')
#             current = current.next
#
#
# a_llist = LinkedList()
# n = int(input('How many elements would you like to add? '))
# for i in range(n):
#     data = int(input('Enter data item: '))
#     a_llist.append(data)
# print('The linked list: ', end='')
# a_llist.display()


def pairs(l1,l2,n):
    pairs=[]
    i=0
    while i<=n:
        if l1[i] + l2[i] == n:
            pairs.append([l1[i],l2[i]])
            i = i + 1
    return pairs

print (pairs([6, 8, 10, 2, 3, 9, 6],[11, 1, 4, 3, 7],10))