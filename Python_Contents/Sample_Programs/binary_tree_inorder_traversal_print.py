class Queue:
    def __init__(self):
        self.items =[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def print_queue(self):
        return self.items

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isempty(self):
        return len(self.items) ==0

    def peek(self):
        return self.items[-1]

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)



# class Node(object):
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinaryTree(object):
#     def __init__(self,data):
#         self.root = Node(data)
#
#     def preorder(self,start,traversal):
#         if start:
#             traversal += (str(start.value) + "" + "--> ")
#             traversal = self.preorder(start.left,traversal)
#             traversal = self.preorder(start.right,traversal)
#         return traversal
#
#     def inorder_traversal_print(self):
#         pass
#     def print_tree_traversal(self,typee):
#         if typee == "preorder":
#             return self.inorder_traversal_print(tree.root,"")
#
#
#
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# print(tree.print_tree_traversal("preorder"))
# print(tree.print_tree_traversal("inorder"))
# print(tree.print_tree_traversal("postorder"))

