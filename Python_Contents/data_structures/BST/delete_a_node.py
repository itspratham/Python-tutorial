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


def inorder(root):
    if root is None:
        return root
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def level_order(root):
    a_Queue = [root]
    while len(a_Queue) > 0:
        popped_item = a_Queue.pop(0)
        print(popped_item.data, end=" ->")
        if popped_item.left:
            a_Queue.append(popped_item.left)
        if popped_item.right:
            a_Queue.append(popped_item.right)
    print("")


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.right.left = Node(1)
print("Original node:")
level_order(root)
result = delete_the_node(root, 3)
print("After deleting specified node:")
level_order(root)
preOrder(root)
print("")
inorder(root)
