# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self):
#         self.head = None
#
#     def inorder(self, start):
#        if start:
#             self.inorder(start.left)
#             print(start.data, end = "-> ")
#             self.inorder(start.right)
#        return
#
# def insertLevelOrder(arr, root, i, n):
#     if i < n:
#         temp = Node(arr[i])
#         root = temp
#         print(root.data,end="- > ")
#         root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
#         root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
#
#
# bt = BinaryTree()
#
# arr = [1,2,3,4,5,6,7,8]
# n= len(arr)
# insertLevelOrder(arr,bt.head,0,n)
#
# bt.inorder(bt.head)











class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.head = None

    def set_root(self,data):
        self.head = Node(data)
        return self.head

    def check_for_root(self,data):
        if self.head is None:
            #self.head = Node(data)
            return False
        else:
            return True

    def search(self,start, ref_data):
        if start.data == ref_data:
            return start
        if start.left is not None:
            temp = self.search(start.left, ref_data)
            if temp is not None:
                return temp
        if start.right is not None:
            temp = self.search(start.right, ref_data)
            if temp is not None:
                return temp
        return None

    def search_for(self,ref_data):
        x =self.search(self.head,ref_data)
        if x is not None:
            return x
        return False

    def insert_left(self,data,ref_data):
        if self.check_for_root(data) == False:
            print("Root is not present")
            return
        node_found = self.search_for(ref_data)
        new_node = Node(data)
        if self.search_for(ref_data):
            node_found.left = new_node
            new_node.left = new_node.left
            new_node.right = None

        else:
            print("Enter the valid node number in the tree. ")
            return
        cur_node =self.head
        new_node = Node(data)
        while cur_node.left != None:
            cur_node = cur_node.left

        cur_node.left = new_node
        new_node.left = None
        new_node.right = None

    def insert_right(self, data):
        if self.check_for_root(data) == False:
            print("Inserted data as root node since root is not present")
            return
        cur_node = self.head
        new_node = Node(data)
        while cur_node.right != None:
            cur_node = cur_node.right

        cur_node.right = new_node
        new_node.left = None
        new_node.right = None

    def inorder(self, start):
       if start:
            self.inorder(start.left)
            print(start.data, end = "-> ")
            self.inorder(start.right)
       return

b = BT()
b.set_root(1)
b.insert_left(2)
b.insert_right(3)
b.insert_left(4)
b.insert_right(5)
b.insert_left(6)
b.insert_right(7)
b.inorder(b.head)
print(b.search_for(7))


