class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m > n:
            return ""

        freq = defaultdict(int)
        for i in t:
            freq[i] += 1

        l = 0
        left = 0
        right = n + 1
        remaining = m

        for r in range(n):
            if freq[s[r]] > 0:
                remaining -= 1
            freq[s[r]] -= 1
            if remaining <= 0:
                if r - l < right - left:
                    left = l
                    right = r
                while r - l + 1 >= m:
                    freq[s[l]] += 1
                    if freq[s[l]] <= 0:
                        l += 1
                        if r - l < right - left:
                            left = l
                            right = r
                    else:
                        freq[s[l]] -= 1
                        break
        return s[left:right + 1] if right - left < n else ""