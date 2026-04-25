from collections import deque


class Graph:


    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def load_from_file(self, filename):

        with open(filename, "r") as file:
            lines = file.readlines()
            self.V = int(lines[0])
            self.graph = {i: [] for i in range(self.V)}

            for line in lines[1:]:
                u, v = map(int, line.split())
                self.add_edge(u, v)


    def topological_sort_kahn(self):

        iterations = 0
        indegree = [0] * self.V

        for node in self.graph:
            for neighbor in self.graph[node]:
                indegree[neighbor] += 1
                iterations += 1

        queue = deque()

        for i in range(self.V):
            if indegree[i] == 0:
                queue.append(i)

            iterations += 1

        topo_order = []

        while queue:

            node = queue.popleft()

            topo_order.append(node)
            iterations += 1

            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1
                iterations += 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    iterations += 1

        if len(topo_order) != self.V:

            return None, iterations

        return topo_order, iterations
