class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def level_order(root):
    a_Queue = [root]
    while len(a_Queue) > 0:
        popped_item = a_Queue.pop(0)
        print(popped_item.data, end=" ->")
        if popped_item.left:
            a_Queue.append(popped_item.left)
        if popped_item.right:
            a_Queue.append(popped_item.right)


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.right.left = Node(1)
level_order(root)
