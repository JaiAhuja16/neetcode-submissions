class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            board[i][j] = '!'
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny] == '!' or board[nx][ny] == 'X':
                    continue
                dfs(nx, ny)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m - 1][i] == 'O':
                dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '!':
                    board[i][j] = 'O'