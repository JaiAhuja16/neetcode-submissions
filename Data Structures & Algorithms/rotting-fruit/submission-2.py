class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    c += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        t = 0
        while c and q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    if x + dx < 0 or x + dx >= m or y + dy < 0 or y + dy >= n or grid[x + dx][y + dy] != 1:
                        continue
                    grid[x + dx][y + dy] = 2
                    q.append((x + dx, y + dy))
                    c -= 1
            t += 1
        return t if c == 0 else -1