class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums)
        c = 0
        while c < n - k:
            print(heapq.heappop(nums))
            c += 1
        return heapq.heappop(nums)