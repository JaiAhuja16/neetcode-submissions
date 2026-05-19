class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mini = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(mini, nums[l])
            mid = l + (r - l) // 2
            mini = min(mini, nums[mid])
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        return mini