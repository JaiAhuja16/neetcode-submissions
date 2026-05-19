class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        n = len(nums1)
        m = len(nums2)
        middle = (n + m - 1) // 2
        while p1 < n and p2 < m and p1 + p2 < middle:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        while p1 < n and p1 + p2 < middle:
            p1 += 1
        while p2 < m and p1 + p2 < middle:
            p2 += 1
        if (n + m) & 1:
            if p1 < n:
                if p2 < m:
                    return min(nums1[p1], nums2[p2])
                return nums1[p1]
            return nums2[p2]
        else:
            if p1 < n:
                if p2 < m:
                    return (nums1[p1] + nums2[p2]) / 2
                return (nums1[p1] + nums1[p1 + 1]) / 2
            return (nums2[p2] + nums2[p2 + 1]) / 2
