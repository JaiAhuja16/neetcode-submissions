class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n - 1 edges, no cycle, all connected
        if len(edges) != n - 1:
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        flag = True
        def dfs(curr, par):
            visited.add(curr)
            for v in adj[curr]:
                if v not in visited:
                    dfs(v, curr)
                elif v != par:
                    flag = False
                    break
        visited = set()
        c = 0
        for i in range(n):
            if i not in visited:
                dfs(i, None)
                c += 1
        if c > 1 or not flag:
            return False
        return True