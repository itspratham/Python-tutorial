# # Python3 Program to print BFS traversal
# # from a given source vertex. BFS(int s)
# # traverses vertices reachable from s.
# from collections import defaultdict
#
#
# # This class represents a directed graph
# # using adjacency list representation
#
#
# class Graph:
#
#     # Constructor
#     def __init__(self):
#
#         # default dictionary to store graph
#         self.graph = defaultdict(list)
#
#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def print_graph(self):
#         return self.graph
#
#     # Function to print a BFS of graph
#     def BFS(self, s):
#
#         # Mark all the vertices as not visited
#         visited = [False] * (max(self.graph) + 1)
#         # Create a queue for BFS
#         queue = [s]
#
#         # Mark the source node as
#         # visited and enqueue it
#         visited[s] = True
#
#         while queue:
#             # Dequeue a vertex from
#             # queue and print it
#             s = queue.pop(0)
#             print(s, end=" ")
#
#             # Get all adjacent vertices of the
#             # dequeued vertex s. If a adjacent
#             # has not been visited, then mark it
#             # visited and enqueue it
#             for i in self.graph[s]:
#                 if not visited[i]:
#                     queue.append(i)
#                     visited[i] = True
#
#
# # Driver code
#
# # Create a graph given in
# # the above diagram
# g = Graph()
# g.addEdge(1, 4)
# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(2, 2)
# g.addEdge(4, 1)
# g.addEdge(4, 6)
# g.addEdge(5, 1)
# g.addEdge(5, 2)
# g.addEdge(5, 6)
#
# print("Following is Breadth First Traversal"
#       " (starting from vertex 2)")
# g.BFS(2)
# print()
# print(g.print_graph())
#
# import collections
#
#
# # BFS algorithm
# def bfs(graph, root):
#     visited, queue = set(), collections.deque([root])
#     visited.add(root)
#
#     while queue:
#
#         # Dequeue a vertex from queue
#         vertex = queue.popleft()
#         print(str(vertex) + " ", end="")
#
#         # If not visited, mark it as visited, and
#         # enqueue it
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)
#
#
# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     print("Following is Breadth First Traversal: ")
#     bfs(graph, 3)
#
# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}
#
#
# def find_path(graph, start, end, path=[]):
#     print(start, "start")
#     path = path + [start]
#     if start == end:
#         return path
#     if not graph.get(start):
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath:
#                 return newpath
#     return None
#
#
# print(find_path(graph, 'D', 'A'))


class Node:
    def __init__(self, data):
        self.data = data
        self.edge = []

    def add_edge(self, edge):
        self.edge.append(edge)

    def traverse(self):
        traversed = []
        queue = []
        for ed in self.edge:
            queue.append(ed)
        # print([i.data for i in queue])
        while len(queue) != 0:
            vertex = queue.pop()
            if vertex not in traversed:
                print(vertex.data, "->", end=" ")
                traversed.append(vertex)
                for ed in vertex.edge:
                    if ed not in queue:
                        queue.append(ed)
            # print([i.data for i in queue])
            # print([i.data for i in traversed])


graphroot = Node(1)

# Lets add a new vertex

vertice4 = Node(4)
vertice2 = Node(2)
vertice3 = Node(3)
graphroot.add_edge(vertice4)
graphroot.add_edge(vertice2)
graphroot.add_edge(vertice3)
vertice2.add_edge(vertice2)

vertice6 = Node(6)
vertice4.add_edge(graphroot)
vertice4.add_edge(vertice6)

vertice5 = Node(5)
vertice5.add_edge(graphroot)
vertice5.add_edge(vertice2)
vertice5.add_edge(vertice6)

vertice6.add_edge(vertice5)

graphroot.traverse()
