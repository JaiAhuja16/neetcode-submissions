class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(i, j):
            visited[i][j] = 1
            curr = 1
            if i > 0 and grid[i - 1][j] == 1 and not visited[i - 1][j]:
                curr += dfs(i - 1, j) 
            if j > 0 and grid[i][j - 1] == 1 and not visited[i][j - 1]:
                curr += dfs(i, j - 1) 
            if i < m - 1 and grid[i + 1][j] == 1 and not visited[i + 1][j]:
                curr += dfs(i + 1, j) 
            if j < n - 1 and grid[i][j + 1] == 1 and not visited[i][j + 1]:
                curr += dfs(i, j + 1)
            return curr

        maxi = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    maxi = max(maxi, dfs(i, j))
        
        return maxi