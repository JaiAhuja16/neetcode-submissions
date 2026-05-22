class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        d = defaultdict(int)
        l = 0
        ans = 1
        maxi = 0
        for i in range(n):
            d[s[i]] += 1
            maxi = max(maxi, d[s[i]])
            while l < i and i - l + 1 - maxi > k:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        return ans