class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = []
        n = len(nums)
        
        def f(index, curr):
            if index == n:
                op.append(curr[:])
                return
            f(index + 1, curr)
            curr.append(nums[index])
            f(index + 1, curr)
            curr.pop()
        f(0, [])
        return op