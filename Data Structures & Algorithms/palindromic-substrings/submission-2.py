class Solution:
    def countSubstrings(self, s: str) -> int:
        # ==========  DP solution (TC, SC = O(n^2), O(n^2)) ======================
        """
        dp[l][r] = True if s[l...r] is palin else False
        
        base case:
            dp[i][i] = True

        recursion:
            dp[l][r] = dp[l + 1][r - 1] and s[l] == s[r]
        """
        # c = 1
        # n = len(s)
        # dp = [[False] * (n + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     dp[i][i] = True
        # for l in range(n - 1, 0, -1):
        #     for r in range(l, n + 1):
        #         dp[l][r] = (dp[l + 1][r - 1] or r - l <= 2) and s[l - 1] == s[r - 1]
        #         c += int(dp[l][r])
        # return c
        # ================================================================

        # ==========  TWO pointer solution (TC, SC = O(n^2), O(1)) ======================
        n = len(s)
        c = 0
        for i in range(n):
            for j in range(min(i + 1, n - i)):
                # print(i - j, i + j)
                if s[i - j] == s[i + j]:
                    c += 1
                else:
                    break
        for i in range(n - 1):
            for j in range(min(i + 1, n - i - 1)):
                # print(i - j, i + j + 1)
                if s[i - j] == s[i + j + 1]:
                    c += 1
                else:
                    break
        return c