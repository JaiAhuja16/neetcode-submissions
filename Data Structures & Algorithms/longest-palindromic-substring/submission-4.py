class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = True
        l, r = 0, 0
        for i in range(n - 1, 0, -1):
            for j in range(i, n + 1):
                dp[i][j] = (dp[i + 1][j - 1] or j - i <= 2) and s[i - 1] == s[j - 1]
                if dp[i][j] and j - i > r - l:
                    l, r = i - 1, j - 1
        # for row in dp:
        #     print(*row)
        return s[l:r + 1]