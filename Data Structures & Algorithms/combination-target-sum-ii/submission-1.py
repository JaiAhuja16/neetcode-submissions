class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        op = []
        nums.sort()
        def f(index, curr, s):
            if s == target:
                op.append(curr)
                return
            for i in range(index, n):
                if (i > index and nums[i - 1] == nums[i]):
                    continue
                if s + nums[i] > target:
                    break
                f(i + 1, curr + [nums[i]], s + nums[i])
        f(0, [], 0)
        return op