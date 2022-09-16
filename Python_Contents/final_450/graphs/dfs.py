from collections import defaultdict

class Stack:
    def __init__(self, a_list=[]):
        self.a_list = a_list

    def insert_an_element(self, value):
        self.a_list.append(value)
        return self.a_list

    def pop_an_element(self):
        if len(self.a_list) > 0:
            return self.a_list.pop()
        return


class Graph:
    def __init__(self, graph):
        self.graf = graph

    def dfs_traversal(self, element, visited_list=[]):
        for item in self.graf[element]:
            if item not in visited_list:
                visited_list.append(item)
            if element not in visited_list:
                visited_list.append(element)
            if item not in self.graf.keys():
                self.dfs_traversal(item, visited_list)
        return visited_list


graph = {'A': ['B', 'Z'],
         'B': ['Z', 'D'],
         'Z': ['D', 'C'],
         'D': ['Z'],
         'E': ['F'],
         'F': ['Z']}
g = Graph(graph)
print(*g.dfs_traversal('A'))
