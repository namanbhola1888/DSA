class ZeroRequestsServer:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key = lambda x: x[1])

        arr = [(val, idx) for idx, val in enumerate(queries)]
        arr.sort(key = lambda x: x[0])

        server_count = {}
        left = 0
        right = 0
        ans = [0] * len(queries)

        for query, idx in arr:
            start = query - x
            end = query

            while right < len(logs) and logs[right][1] <= end:
                server_id = logs[right][0]
                server_count[server_id] = server_count.get(server_id, 0) + 1
                right+=1

            while left < right and logs[left][1] < start:
                server_id = logs[left][0]
                server_count[server_id] -= 1

                if server_count.get(server_id) == 0:
                    del server_count[server_id]

                left+=1

            ans[idx] = n - len(server_count)

        return ans


n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [5,11]

obj = ZeroRequestsServer()
print(obj.countServers(n, logs, x, queries))