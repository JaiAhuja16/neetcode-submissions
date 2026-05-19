class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(rate : int) -> bool:
            return sum(math.ceil(i / rate) for i in piles) <= h

        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans