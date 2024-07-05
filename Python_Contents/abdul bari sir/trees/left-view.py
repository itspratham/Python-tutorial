class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def left_view(root):
    if root is None:
        return

    while root:
        print(root.data)
        root = root.left

def right_view(root):
    if root is None:
        return

    while root:
        print(root.data)
        root = root.right

def top_view(root):
    if root is None:
        return
    root1 = root
    while root:
        print(root.data)
        root = root.right
        print(root.left.data)

def bottom_view(root):
    if root is None:
        return
    while root:
        if root.left is None:
            print(root.data)
            root = root.right
        else:
            root = root.left
        if root.right is None:
            print(root.data)
            root = root.left
        else:
            root = root.right

class Tree(Node):
    def __init__(self, data):
        self.root1 = Node(data)
        super().__init__(data)


root = Tree(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

bottom_view(root)
