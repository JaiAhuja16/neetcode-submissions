class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) 
        memo = defaultdict(lambda : -1)

        def dfs(ind, last):
            if ind == n:
                return 0
            if memo[(ind, last)] != -1:
                return memo[(ind, last)]
            c1 = 0
            if nums[ind] > last:
                c1 = 1 + dfs(ind + 1, nums[ind])
            c2 = dfs(ind + 1, last)
            memo[(ind, last)] = max(c1, c2)
            return memo[(ind, last)]
        return dfs(0, -float('inf'))