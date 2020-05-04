class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = None

    def inorder(self, start):
       if start:
            self.inorder(start.left)
            print(start.data, end = "-> ")
            self.inorder(start.right)
       return

def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        print(root.data,end="- > ")
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)


bt = BinaryTree()

arr = [1,2,3,4,5,6,7,8]
n= len(arr)
insertLevelOrder(arr,bt.head,0,n)

bt.inorder(bt.head)
