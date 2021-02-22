# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self,data):
#         if self.head is None:
#             self.head = Node(data)
#             return
#         cur_node = self.head
#         new_node = Node(data)
#         while cur_node.next:
#             cur_node = cur_node.next
#         cur_node.next =new_node
#
#
#     def print_list(self):
#         currnode = self.head
#         while currnode:
#             print(currnode.data)
#             currnode = currnode.next
#
#     def delete_node(self,key):
#         if self.head is None:
#             print("No scope to delete the node")
#             return
#         curr_node = self.head
#         if curr_node.data == key:
#             self.head = curr_node.next
#             curr_node = None
#             return
#
#         prev = None
#         while curr_node.data and curr_node.data != key:
#             prev = curr_node
#             curr_node = curr_node.next
#
#         prev.next = curr_node.next
#         curr_node = None
#
#     def insert_at_an_index(self,position,data):
#         newnode = Node(data)
#         if self.head is None:
#             print("List is empty and I can insert for you at 1st position")
#             self.append(data)
#             return
#         curr_node = self.head
#         if self.head.next is None and position == 1:
#             self.head = newnode
#             newnode.next = curr_node
#             return
#         prev = None
#         count = 1
#         while count<position:
#             prev = curr_node
#             curr_node = curr_node.next
#             count = count+1
#         prev.next = newnode
#         newnode.next = curr_node
#
#     def rotate_left(self,position):
#         if self.head is None and position<=0:
#             return
#         if self.head and position==1:
#             return
#
#         headd = self.head
#         curr_node = self.head
#         prev = None
#         count = 0
#         while curr_node and count<position:
#             prev = curr_node
#             headd = headd.next
#             curr_node = curr_node.next
#             count = count + 1
#         curr_node = prev
#
#         while headd:
#             prev =headd
#             headd = headd.next
#
#         headd = prev
#         headd.next = self.head
#         self.head = curr_node.next
#         curr_node.next = None
#
#     def prepend(self,data):
#         if self.head == None:
#             self.head = Node(data)
#             self.head.next = None
#             return
#         newnode = Node(data)
#         curnode = self.head
#         self.head = newnode
#         newnode.next = curnode
#
# l = LinkedList()
# l.append("A")
# l.prepend("B")
# l.append("C")
# l.append("D")
# l.append("E")
# l.print_list()



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
        curnode =self.head
        while curnode:
            print(curnode.data)
            curnode= curnode.next

    def prepend(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        newnode= Node(data)
        curnode = self.head
        self.head = newnode
        newnode.next = curnode

    def length(self):
        if self.head is None:
            return 0
        curnode = self.head
        count =1
        while curnode.next:
            count = count + 1
            curnode = curnode.next
        return count

    def middle_ele(self):
        count = self.length()
        position = count//2
        curnode =self.head
        countt=1
        while countt<position:
            curnode = curnode.next
            countt+=1
        return curnode.next.data

    def sortList(self):
        # swap = 0
        if self.head != None:
            while (1):

                swap = 0
                tmp = self.head
                while (tmp.next != None):
                    if tmp.data > tmp.next.data:
                        # swap them
                        swap += 1
                        p = tmp.data
                        tmp.data = tmp.next.data
                        tmp.next.data = p
                        tmp = tmp.next
                    else:
                        tmp = tmp.next

                if swap == 0:
                    break
                else:
                    continue

            return self.head
        else:
            return self.head

ll = LinkedList()
ll.append(1)
ll.append(2)
#ll.prepend(3)
ll.append(5)
ll.append(87)
#ll.prepend(89)
#ll.sortList()
ll.print_list()

