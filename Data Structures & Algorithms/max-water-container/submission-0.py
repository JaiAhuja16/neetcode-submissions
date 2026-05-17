class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        maximise -> min(hi, hj) * (j - i)
        """
        n = len(height)
        l = 0
        r = n - 1
        maxi = 0
        while l < r:
            maxi = max(maxi, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxi