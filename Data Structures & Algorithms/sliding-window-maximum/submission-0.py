class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        ind = set(range(k))
        l = 1
        r = k
        op = [None] * (n - k + 1)
        for _ in range(n - k + 1):
            num, ind = heapq.heappop(heap)
            for j in range(max(0, ind - k + 1), min(ind, n - k) + 1):
                if op[j] == None:
                    op[j] = -num
        return op