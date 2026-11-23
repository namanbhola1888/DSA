class DFS:
    def __init__(self, graph):
        self.graph = graph


    def dfs(self, start):
        visited = set()

        return self.dfs_recursive(start, visited)


    def dfs_recursive(self, node, visited):
        visited.add(node)
        print(f"{node} ->", end=" ")

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)


    def dfs_iterative(self, start):
        visited = set()
        stack = []

        stack.append(start)

        while stack:
            top = stack.pop()

            if top not in visited:
                visited.add(top)
                print(f"{top} ->",end=" ")

                for neighbour in self.graph[top]:
                    if neighbour not in visited:
                        stack.append(neighbour)



graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

obj = DFS(graph)

obj.dfs(0)

