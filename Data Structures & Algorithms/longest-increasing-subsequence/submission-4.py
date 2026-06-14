from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) 
        @cache
        def dfs(ind, last):
            if ind == n:
                return 0
            c1 = 0
            if last == -1 or nums[ind] > nums[last]:
                c1 = 1 + dfs(ind + 1, ind)
            c2 = dfs(ind + 1, last)
            return max(c1, c2)
        return dfs(0, -1)