class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        op = []
        n = len(nums)
        nums.sort()
        def f(index, curr):
            if index == n:
                op.append(curr[:])
                return
            curr.append(nums[index])
            f(index + 1, curr)
            curr.pop()
            while index < n - 1 and nums[index] == nums[index + 1]:
                index += 1
            f(index + 1, curr)
        f(0, [])
        return op