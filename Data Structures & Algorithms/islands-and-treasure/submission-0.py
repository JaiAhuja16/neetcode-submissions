class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0])
        c = 0
        while q:
            c += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != INF:
                        continue
                    grid[nx][ny] = c
                    q.append((nx, ny))
        