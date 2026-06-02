class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for l in range(1, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                dp[i][j] = int(s[i - 1] == s[j - 1] and (dp[i + 1][j - 1] if j - i >= 2 else True))
        maxi = 1
        l, r = 0, 0
        for i in range(1, n):
            for j in range(n, i, -1):
                if dp[i][j] and j - i + 1 > maxi:
                    maxi = j - i + 1
                    l = i - 1
                    r = j - 1
                    break
        # for i in dp:
        #     print(*i)
        return s[l:r + 1]