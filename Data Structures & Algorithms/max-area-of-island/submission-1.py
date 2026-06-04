class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            curr = 1
            if i > 0 and grid[i - 1][j] == 1:
                curr += dfs(i - 1, j) 
            if j > 0 and grid[i][j - 1] == 1:
                curr += dfs(i, j - 1) 
            if i < m - 1 and grid[i + 1][j] == 1:
                curr += dfs(i + 1, j) 
            if j < n - 1 and grid[i][j + 1] == 1:
                curr += dfs(i, j + 1)
            return curr

        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxi = max(maxi, dfs(i, j))
        
        return maxi