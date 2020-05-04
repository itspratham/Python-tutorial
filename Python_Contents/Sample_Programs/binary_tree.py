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
#             traversal += (str(start.value) +  + "--> ")
#             traversal = self.preorder(start.left,traversal)
#             traversal = self.preorder(start.right,traversal)
#         return traversal
#
#     def inorder(self,start,traversal):
#         if start:
#             traversal = self.inorder(start.left, traversal)
#             traversal += (str(start.value) +  + "--> ")
#             traversal = self.inorder(start.right, traversal)
#         return traversal
#
#     def postorder(self, start, traversal):
#         if start:
#             traversal = self.postorder(start.left, traversal)
#             traversal = self.postorder(start.right, traversal)
#             traversal += (str(start.value) +  + "--> ")
#         return traversal
#
#     def print_tree_traversal(self,typee):
#         if typee == "preorder":
#             return self.preorder(tree.root,)
#         elif typee == "inorder":
#             return self.inorder(tree.root,)
#         elif typee == "postorder":
#             return self.postorder(tree.root,)
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


# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
# new node
# class newNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None
#
#
# # Function to insert nodes in level order
# def insertLevelOrder(arr, root, i, n):
#     # Base case for recursion
#     if i < n:
#         temp = newNode(arr[i])
#         root = temp
#         # insert left child
#         print(root.data,end="--> ")
#         root.left = insertLevelOrder(arr, root.left,
#                                      2 * i + 1, n)
#         # insert right child
#         root.right = insertLevelOrder(arr, root.right,
#                                       2 * i + 2, n)
#     return root
#
#
# # Function to print tree nodes in
# # InOrder fashion
# def preorder(root):
#     if root != None:
#         print(root.data, end="--> ")
#         preorder(root.left)
#         preorder(root.right)
#
#     # Driver Code

# def inorder(root):
#     if root != None:
#         inorder(root.left)
#         print(root.data, end="--> ")
#         inorder(root.right)
#
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
#     n = len(arr)
#     root = None
#     root = insertLevelOrder(arr, root, 0, n)
#     print()
#     preorder(root)
#     print()
#     inorder(root)



# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.left = None
#         self.right =None
#
# class BinaryTree(object):
#     def __init__(self):
#         self.root = None
#
#     def insert(self,arr):
#         if self.root is None:
#             self.root = Node(arr[0])
#         self._insert(arr,self.root,1,len(arr))
#
#     def _insert(self,arr,curnode,i,n):
#         while i<n:
#             temp = Node(arr[i])
#             root = temp
#             root.left = self._insert(arr,root.left,2*i+1,n)
#             root.right = self._insert(arr,root.right,2*i+2,n)
#             print(root.data)
#         return root
#
#
#
#     def preorder(self,root):
#         if root != None:
#             print(root.data, end="--> ")
#             self.preorder(root.left)
#             self.preorder(root.right)
# b= BinaryTree()
# b.insert([1,2,3,4,5,6,7])
# b.preorder(b.root)


# class Node:
#     def __init__(self,dta=None):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self,data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(data,self.root)
#
#     def _insert(self, data, cur_node):
#         if data < cur_node.data:
#             if cur_node.left is None:
#                 cur_node.left = Node(data)
#             else:
#                 self._insert(data, cur_node.left)
#         elif data>cur_node.data:
#             if cur_node.right is None:
#                 cur_node.right = Node(data)
#             else:
#                 self._insert(data, cur_node.right)
#         else:
#             print("Value is already in the binary tree")
#
#     def preorder(self, root):
#         if root != None:
#             print(root.data, end=" -->")
#             self.preorder(root.left)
#             self.preorder(root.right)
#
# b = BST()
# b.insert(23)
# b.insert(45)
# b.insert(20)
# b.insert(56)
# b.insert(76)
# b.preorder(b.root)


# Represent a node of binary tree
# class Node:
#     def __init__(self, data):
#         # Assign data to the new node, set left and right children to None
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         # Represent the root of binary tree
#         self.root = None
#
#     # insertNode() will add new node to the binary tree
#     def insertNode(self, data):
#         # Create a new node
#         newNode = Node(data)
#
#         # Check whether tree is empty
#         if (self.root == None):
#             self.root = newNode
#             return
#         else:
#             queue = []
#             # Add root to the queue
#             queue.append(self.root)
#
#             while (True):
#                 node = queue.pop(0)
#                 # If node has both left and right child, add both the child to queue
#                 if (node.left != None and node.right != None):
#                     queue.append(node.left)
#                     queue.append(node.right)
#                 else:
#                     # If node has no left child, make newNode as left child
#                     if (node.left == None):
#                         node.left = newNode
#                         queue.append(node.left)
#                     else:
#                         # If node has left child but no right child, make newNode as right child
#                         node.right = newNode
#                         queue.append(node.right)
#                     break
#
#                     # inorder() will perform inorder traversal on binary search tree
#
#     def inorderTraversal(self, node):
#         if node != None:
#             self.inorderTraversal(node.left)
#             self.inorderTraversal(node.right)
#             print(node.data, end="-- >")
#
#
# bt = BinaryTree()
# bt.insertNode(1)
# bt.insertNode(2)
# bt.insertNode(3)
# bt.insertNode(4)
# bt.insertNode(5)
# bt.insertNode(6)
# bt.insertNode(7)
# bt.inorderTraversal(bt.root)




#
# class Node:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None
#
#
# class BST:
#     def __init__(self, root):
#         self.root = root
#
#     def pre_order(self, start, traversal):
#         if start !=None:
#             print(start.value, end="--> ")
#             traversal = self.pre_order(start.left, traversal)
#             traversal = self.pre_order(start.right, traversal)
#         return traversal
#
#
# def arr_to_tree(arr, root, i, n):
#     if i < n:
#         temp = Node(arr[i])
#         root = temp
#         root.left = arr_to_tree(arr, root.left, 2*i+1, n)
#         root.right = arr_to_tree(arr, root.left, 2*i+2, n)
#     return root
#
#
# def main():
#     li = [1,2,3,4,5,6,7,8]
#
#     root = None
#     root = arr_to_tree(li, root, 0, len(li))
#
#     bst = BST(root)
#     print(bst.pre_order(root, " "))
#
#
# if __name__ == '__main__':
#     main()
