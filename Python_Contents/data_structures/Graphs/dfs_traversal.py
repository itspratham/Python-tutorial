class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        return self.list.append(data)

    def pop(self):
        return self.list.pop()

    def if_empty(self):
        return 1 if len(self.list) == 0 else 0


class Graph:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def add_edge(self, data):
        return self.edges.append(data)

    def traversal(self,graphroot,  stack, visited):
        if stack.if_empty():
            return
        else:
            print(graphroot.data)
            visited[graphroot.data] = 1
            if visited[graphroot.data]:
                for i in graphroot.edges:
                    if i not in visited:
                        stack.push(i)
                        self.traversal(graphroot.data, stack, visited)
                stack.pop()
            # self.traversal(graphroot.data, stack, visited)




graphroot = Graph(1)

# Lets add a new vertex

vertice4 = Graph(4)
vertice2 = Graph(2)
vertice3 = Graph(3)
graphroot.add_edge(vertice4)
graphroot.add_edge(vertice2)
graphroot.add_edge(vertice3)
vertice2.add_edge(vertice2)

vertice6 = Graph(6)
vertice4.add_edge(graphroot)
vertice4.add_edge(vertice6)

vertice5 = Graph(5)
vertice5.add_edge(graphroot)
vertice5.add_edge(vertice2)
vertice5.add_edge(vertice6)

vertice6.add_edge(vertice5)

stack = Stack()
stack.push(graphroot)
graphroot.traversal(graphroot, stack, visited = {})
