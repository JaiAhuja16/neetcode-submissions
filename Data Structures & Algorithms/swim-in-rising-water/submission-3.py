class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        
        def possible(i, j, flow):
            if visited[i][j] or grid[i][j] > flow:
                return False
            if i == n - 1 and j == n - 1:
                return True
            visited[i][j] = 1
            if i < n - 1 and possible(i + 1, j, flow):
                return True
            if j < n - 1 and possible(i, j + 1, flow):                
                return True
            if i > 0 and possible(i - 1, j, flow):
                return True
            if j > 0 and possible(i, j - 1, flow):
                return True
            return False

        l = max(grid[0][0], grid[-1][-1])
        r = max(max(i) for i in grid)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if possible(0, 0, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
            for i in range(n):
                for j in range(n):
                    visited[i][j] = 0
        return ans