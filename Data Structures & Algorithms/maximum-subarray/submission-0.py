class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        op = nums[0]
        curr = op
        for i in nums[1:]:
            curr = max(i, curr + i)
            op = max(curr, op)
        return op