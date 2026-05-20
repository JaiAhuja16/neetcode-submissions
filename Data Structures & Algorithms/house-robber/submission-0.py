class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        for i in range(n - 2, -1, -1):
            nums[i] = max(nums[i + 1], nums[i + 2] + nums[i])
        return max(nums[0], nums[1])