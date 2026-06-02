class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for j in nums:
            for i in range(s // 2, j - 1, -1):
                dp[i] |= dp[i - j]
        # print(*dp)
        return dp[s // 2]