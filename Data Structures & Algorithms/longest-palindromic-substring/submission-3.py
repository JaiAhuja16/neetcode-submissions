class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = True
        left, right = 0, 0
        for l in range(1, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                dp[i][j] = (s[i - 1] == s[j - 1] and (dp[i + 1][j - 1] if j - i >= 2 else True))
                if dp[i][j] and j - i > right - left:
                    left, right = i - 1, j - 1
        return s[left:right + 1]