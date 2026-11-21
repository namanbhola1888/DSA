class GraphList:
    def __init__(self):
        self.graph = {}


    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

        else:
            return "Already existed"


    def addEdge(self, u, v):
        if u not in self.graph or v not in self.graph:
            return "Both vertices should exist"

        if v not in self.graph[u]:
            self.graph[u].append(v)

        if u not in self.graph[v]:
            self.graph[v].append(u)


    def removeVertex(self, vertex):
        if vertex not in self.graph:
            return "No such vertex exists"

        for neighbour in self.graph[vertex]:
            self.graph[neighbour].remove(vertex)

        del self.graph[vertex]


    def removeEdge(self, u, v):
        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)

            if u in self.graph[v]:
                self.graph[v].remove(u)


    def hasVertex(self, vertex):
        return vertex in self.graph


    def hasEdge(self, u, v):
        return u in self.graph[v] and v in self.graph[u]


    def getNeighbours(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]

        return []


    def display(self):
        for vertex, neighbours in self.graph.items():
            print(f"{vertex} -> {neighbours}")



g = GraphList()

g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')


g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'D')

g.display()

print("Has vertex A:", g.hasVertex('A'))
print("Has edge A-B:", g.hasEdge('A', 'B'))
print("Neighbors of A:", g.getNeighbours('A'))

g.removeEdge('A', 'B')
g.removeVertex('D')

print("\nAfter deletion:")
g.display()
