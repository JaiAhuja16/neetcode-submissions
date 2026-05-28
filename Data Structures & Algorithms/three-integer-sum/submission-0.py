class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(*nums)
        op = set()
        n = len(nums)
        for i in range(1, n - 1):
            l, r = 0, n - 1
            while l < i and i < r:
                if nums[l] + nums[i] + nums[r] == 0:
                    op.add((nums[l], nums[i], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return [list(i) for i in op]