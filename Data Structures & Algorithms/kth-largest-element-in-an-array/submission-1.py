
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = []
        mid = []
        right = []
        pivot = random.choice(nums)
        for i in nums:
            if i > pivot:
                left.append(i)
            elif i < pivot:
                right.append(i)
            else:
                mid.append(i)

        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))
        return pivot