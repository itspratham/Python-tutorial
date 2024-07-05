# Definition: Binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minimum(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def maximum(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)
print(maximum(root))