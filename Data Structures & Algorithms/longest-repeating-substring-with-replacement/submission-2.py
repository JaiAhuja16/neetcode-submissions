class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        d = defaultdict(int)
        l = 0
        ans = 1
        for i in range(n):
            d[s[i]] += 1
            while l < i and i - l + 1 - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        return ans