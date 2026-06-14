class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        st = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(max(0, i - 20), i + 1):
                if dp[j] and s[j:i] in st:
                    dp[i] = True
        # print(*dp)
        return dp[n]