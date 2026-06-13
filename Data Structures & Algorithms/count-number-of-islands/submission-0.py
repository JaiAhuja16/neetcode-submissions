class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class DSU:
            def __init__(self, m, n):
                self.par = [[[i, j] for j in range(n)] for i in range(m)]

            def find(self, i, j):
                row, col = i, j
                while self.par[row][col] != [row, col]:
                    row, col = self.par[row][col]
                return self.par[row][col]

            def union(self, i1, j1, i2, j2):
                pi1, pj1 = self.find(i1, j1)
                pi2, pj2 = self.find(i2, j2)
                if pi1 == pi2 and pj1 == pj2:
                    return False
                self.par[pi2][pj2] = [pi1, pj1]
                return True

        m, n = len(grid), len(grid[0])
        dsu = DSU(m, n)
        total = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    total += 1
                    for dx, dy in dirs:
                        if i + dx < 0 or i + dx >= m or j + dy < 0 or j + dy >= n or grid[i + dx][j + dy] == '0':
                            continue
                        if dsu.union(i, j, i + dx, j + dy):
                            total -= 1
        return total
