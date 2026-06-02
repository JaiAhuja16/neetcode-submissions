class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if visited[node]:
                return False
            visited[node] = 1
            for v in adj[node]:
                if v == par:
                    continue
                if not dfs(v, node):
                    return False
            return True

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [0] * (n + 1)
            if not dfs(u, None):
                return [u, v]
        return []