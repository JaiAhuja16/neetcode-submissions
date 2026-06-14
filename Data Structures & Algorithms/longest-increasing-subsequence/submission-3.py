from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(100000)
        def dfs(ind, last):
            if ind == n:
                return 0
            c1 = 0
            if nums[ind] > last:
                c1 = 1 + dfs(ind + 1, nums[ind])
            c2 = dfs(ind + 1, last)
            return max(c1, c2)
        return dfs(0, -float('inf'))