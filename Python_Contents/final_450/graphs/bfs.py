from collections import defaultdict


class Graph:
    def __init__(self, graph):
        self.graf = graph

    def bfs_traversal(self):
        visited_list = []
        for item, listt in self.graf.items():
            if item not in visited_list:
                visited_list.append(item)
            for itemm in listt:
                if itemm not in visited_list:
                    visited_list.append(itemm)
        return visited_list


graph = {'A': ['B', 'Z'],
         'B': ['Z', 'D', 'C'],
         'Z': ['D'],
         'D': ['Z'],
         'E': ['F'],
         'F': ['Z']}
g = Graph(graph)
print(*g.bfs_traversal())
