class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        op = []
        l = 0
        q = deque()
        for r in range(n):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r - l + 1 == k:
                op.append(nums[q[0]])
                l += 1
        return op