class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        op = [1] * n
        prefix = 1
        for i in range(n):
            op[i] *= prefix
            prefix *= nums[i]
        prefix = nums[n - 1]
        for i in range(n - 2, -1, -1):
            op[i] *= prefix
            prefix *= nums[i]
        return op