class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            n = len(nums)
            op = []
            def f(L, s):
                if len(L) == n:
                    op.append(L[:])
                    return
                for i in nums:
                    if i not in s:
                        L.append(i)
                        s.add(i)
                        f(L, s)
                        L.pop()
                        s.remove(i)
            f([], set())
            return op