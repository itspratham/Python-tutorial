# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert
# a new node with the given key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif key > root.val:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)



def find_the_value(root, target):
    if root is None:
        return False
    else:
        if root.val == target:
            return True
        elif target > root.val:
            find_the_value(root.right, target)
            find_the_value(root.left, target)
        else:
            find_the_value(root.left, target)
            find_the_value(root.right, target)


# Driver program to test the above functions
# Let us create the following BST
#     50
#  /	 \
# 30	 70
# / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
inorder(r)
print(find_the_value(r, 80))
