class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        op = []
    
        def f(index, curr, s):
            if s == target:
                op.append(curr)
                return
            if s > target:
                return
            for i in range(index, n):
                f(i, curr + [nums[i]], s + nums[i])
        f(0, [], 0)
        return op