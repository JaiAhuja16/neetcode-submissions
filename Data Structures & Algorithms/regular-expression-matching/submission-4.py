class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # def f(i, j):
        #     if j == n:
        #         return i == m
        #     if j < n - 1 and p[j + 1] == '*':
        #         return f(i, j + 2) or (i < m and (p[j] == '.' or s[i] == p[j]) and f(i + 1, j))
        #     if i < m and (p[j] == '.' or s[i] == p[j]):
        #         return f(i + 1, j + 1)
        #     return False
        
        # return f(0, 0)
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                f = i < m and (p[j] == '.' or s[i] == p[j])
                if j < n - 1 and p[j + 1] == '*':
                    dp[i][j] |= dp[i][j + 2]
                    dp[i][j] |= f and dp[i + 1][j]
                elif f:
                    dp[i][j] |= dp[i + 1][j + 1]
        return dp[0][0]