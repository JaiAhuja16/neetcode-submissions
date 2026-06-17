sys.setrecursionlimit(5000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def reach(index):
            if index >= n - 1:
                return True
            if index in memo:
                return memo[index]
            if nums[index] == 0:
                memo[index] = False
                return False
            memo[index] = False
            for i in range(1, nums[index] + 1):
                memo[index] |= reach(index + i)
            return memo[index]
        return reach(0)