class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def delete_the_node(root, target):
    if root is None:
        return root
    if root.data > target:
        root.left = delete_the_node(root.left, target)
    elif root.data < target:
        root.right = delete_the_node(root.right, target)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        number_to_replaced = find_max(root)
        root.data = number_to_replaced.data
        root.left = delete_the_node(root.left, number_to_replaced.data)
    return root


def find_max(root):
    while root.left is not None:
        root = root.left
    return root


def preOrder(root):
    if root is None:
        return root
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.right.left = Node(7)
print("Original node:")
preOrder(root)
result = delete_the_node(root, 3)
print("After deleting specified node:")
preOrder(result)
