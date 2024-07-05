# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def find_the_element(root, target):
#     if root is None:
#         return root
#     if root.data == target:
#         return "Found"
#     if root.data > target:
#         return find_the_element(root.left, target)
#     return find_the_element(root.right, target)
#
# def deleting_a_node(root, to_be_deleted):
#     if root is None:
#         return None
#     if root.data == to_be_deleted:
#
#     if root.data > to_be_deleted:
#
#
#
# root = Node(8)
# root.left = Node(3)
# root.right = Node(10)
# root.left.left = Node(1)
# root.right.right = Node(14)
# root.left.right = Node(6)
# root.right.right.left = Node(13)
# root.left.right.left = Node(4)
# root.left.right.right = Node(7)
# print(find_the_element(root, 12))


# Definition: Binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def delete_Node(root, key):
    # if root doesn't exist, just return it
    if not root:
        return root
    # Find the node in the left subtree	if key value is less than root value
    if root.val > key:
        root.left = delete_Node(root.left, key)
    # Find the node in right subtree if key value is greater than root value,
    elif root.val < key:
        root.right = delete_Node(root.right, key)
    # Delete the node if root.value == key
    else:
        # If there is no right children delete the node and new root would be root.left
        if not root.right:
            return root.left
        # If there is no left children delete the node and new root would be root.right
        if not root.left:
            return root.right
        # If both left and right children exist in the node replace its value with
        # the minimum value in the right subtree. Now delete that minimum node
        # in the right subtree
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        # Delete the minimum node in right subtree
        root.right = delete_Node(root.right, root.val)
    return root


def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)
print("Original node:")
preOrder(root)
result = delete_Node(root, 4)
print("After deleting specified node:")
preOrder(result)
