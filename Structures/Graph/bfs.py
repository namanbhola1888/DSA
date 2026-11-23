from collections import deque

class BFS:
    def __init__(self, graph):
        self.graph = graph


    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:
            front = queue.popleft()
            print(f"{front} ->", end=" ")

            for neighbour in self.graph[front]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

obj = BFS(graph)

obj.bfs(0)
