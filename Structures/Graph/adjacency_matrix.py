class GraphMatrix:
    def __init__(self):
        self.graph = []
        self.vertices = []
        self.vertex_index = {}


    def addVertex(self, vertex):
        if vertex in self.vertex_index:
            return "Already Existed"

        self.vertices.append(vertex)

        for row in self.graph:
            row.append(0)

        self.graph.append([0] * len(self.vertices))

        self.vertex_index[vertex] = len(self.vertices) - 1


    def addEdge(self, u ,v):
        if u not in self.vertex_index or v not in self.vertex_index:
            return "Both should exist"

        i = self.vertex_index[u]
        j = self.vertex_index[v]

        self.graph[i][j] = 1
        self.graph[j][i] = 1


    def removeVertex(self, vertex):
        if vertex not in self.vertices:
            return "No such vertex exists"

        index = self.vertex_index[vertex]

        self.graph.pop(index)

        for row in self.graph:
            row.pop(index)

        self.vertices.pop(index)

        self.vertex_index = {
            v: i for i, v in enumerate(self.vertices)
        }


    def removeEdge(self, u, v):
        if u not in self.vertex_index or v not in self.vertex_index:
            return "No edge exists"

        i = self.vertex_index[u]
        j = self.vertex_index[v]

        self.graph[i][j] = 0
        self.graph[j][i] = 0


    def hasVertex(self, vertex):
        return vertex in self.vertex_index


    def hasEdge(self, u, v):
        if u not in self.vertex_index or v not in self.vertex_index:
            return False

        i = self.vertex_index[u]
        j = self.vertex_index[v]

        return self.graph[i][j] == 1


    def getNeighbours(self, vertex):
        if vertex not in self.vertex_index:
            return []

        i = self.vertex_index[vertex]
        neighbours = []

        for j in range(len(self.vertices)):
            if self.graph[i][j] == 1:
                neighbours.append(self.vertices[j])

        return neighbours


    def display(self):
        print("  ", self.vertices)

        for i, row in enumerate(self.graph):
            print(self.vertices[i], row)



g = GraphMatrix()


g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')

print("Initial Graph:")
g.display()


g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'D')

print("\nGraph after adding edges:")
g.display()


print("\nHas vertex A:", g.hasVertex('A'))
print("Has vertex E:", g.hasVertex('E'))


print("\nHas edge A-B:", g.hasEdge('A', 'B'))
print("Has edge A-D:", g.hasEdge('A', 'D'))


print("\nNeighbours of A:", g.getNeighbours('A'))
print("Neighbours of D:", g.getNeighbours('D'))


g.removeEdge('A', 'B')

print("\nAfter removing edge A-B:")
g.display()


g.removeVertex('D')

print("\nAfter removing vertex D:")
g.display()


# 8. Verify after deletion
print("\nHas vertex D:", g.hasVertex('D'))
print("Has edge B-D:", g.hasEdge('B', 'D'))
print("Neighbours of C:", g.getNeighbours('C'))
