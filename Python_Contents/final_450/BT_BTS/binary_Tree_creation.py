class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def proper_the_traversal(gg):
    gg = gg.split("-->")
    star = '-->'.join(gg[0:-1])
    return star


class BT:
    def createTree(self):
        data = int(input("Enter the data: "))
        if data == -1:
            return None
        root = Node(data)

        print("Enter the left data for {}: ".format(data))
        root.left = self.createTree()

        print("Enter the right data for {}: ".format(data))
        root.right = self.createTree()
        return root

    def pre_order(self, start, traversal):
        if start:
            traversal += str(start.data) + "-->"
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        if start:
            traversal = self.post_order(start.right, traversal)
            traversal += str(start.data) + "-->"
            traversal = self.post_order(start.left, traversal)
        return traversal


f = BT()
g = f.createTree()
gg = f.pre_order(g, "")
print(proper_the_traversal(gg))
