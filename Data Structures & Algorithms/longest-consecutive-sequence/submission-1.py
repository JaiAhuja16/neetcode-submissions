class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        used = defaultdict(int)
        s = set(nums)
        maxi = 0
        for i in nums:
            if used[i]:
                continue
            if i - 1 not in s:
                curr = i
                while not used[curr] and curr in s:
                    used[curr] = 1
                    curr += 1
                maxi = max(maxi, curr - i)
        return maxi