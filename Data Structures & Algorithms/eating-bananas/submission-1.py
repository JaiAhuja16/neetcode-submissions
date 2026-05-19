class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if sum(math.ceil(i / mid) for i in piles) <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans