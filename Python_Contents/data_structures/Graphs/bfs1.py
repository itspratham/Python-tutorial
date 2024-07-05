from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, v):
        visited = [False] * (len(self.graph))
        queue = [v]
        visited[v] = True
        print(visited)
        while queue:
            popped_item = queue.pop(0)
            print(popped_item)
            for i in self.graph[popped_item]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfs(2)
