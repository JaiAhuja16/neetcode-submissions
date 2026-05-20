class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = 0
        b = 0
        c1 = 0
        for i in range(1, len(nums)):
            c1 = max(a + nums[i], b)
            a = b
            b = c1
        a = 0
        b = 0
        c2 = 0
        for i in range(len(nums) - 1):
            c2 = max(a + nums[i], b)
            a = b
            b = c2
        return max(c1, c2)