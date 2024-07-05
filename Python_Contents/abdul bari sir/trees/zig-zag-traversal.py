class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def level_order_traversal(root):
    if root is None:
        return
    a_list = [root]
    count = 0
    while len(a_list) > 0:
        print(a_list[0].data, end="->")
        nn = a_list.pop(0)
        if count % 2 == 0:
            if nn.right is not None:
                a_list.append(nn.right)
            if nn.left is not None:
                a_list.append(nn.left)
        if count % 2 == 1:
            if nn.left is not None:
                a_list.append(nn.left)
            if nn.right is not None:
                a_list.append(nn.right)


        count = count+1


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

level_order_traversal(root)
