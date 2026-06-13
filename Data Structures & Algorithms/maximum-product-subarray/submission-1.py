class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi, mini = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, n):
            if nums[i] == 0:
                ans = max(ans, 0)
                maxi, mini = 1, 1
                continue
            temp = maxi * nums[i]
            maxi = max(temp, mini * nums[i], nums[i])
            mini = min(temp, mini * nums[i], nums[i])
            ans = max(ans, maxi, mini)
        return ans