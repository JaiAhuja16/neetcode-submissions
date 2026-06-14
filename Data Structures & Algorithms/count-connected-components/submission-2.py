class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(curr):
            visited.add(curr)
            for v in adj[curr]:
                if v not in visited:
                    dfs(v)
        visited = set()
        c = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                c += 1
        return c