class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        dp[l][r] = True if s[l...r] is palin else False
        
        base case:
            dp[i][i] = True

        recursion:
            dp[l][r] = dp[l + 1][r - 1] and s[l] == s[r]
        """
        c = 1
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = True
        for l in range(n - 1, 0, -1):
            for r in range(l, n + 1):
                dp[l][r] = (dp[l + 1][r - 1] or r - l <= 2) and s[l - 1] == s[r - 1]
                c += int(dp[l][r])
        return c