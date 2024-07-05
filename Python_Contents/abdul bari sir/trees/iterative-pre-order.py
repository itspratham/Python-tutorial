class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def iterative_preorder(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)

        # Push right child first so that the left is processed first (since stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Example usage:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Iterative Pre-order Traversal:")
iterative_preorder(root)
