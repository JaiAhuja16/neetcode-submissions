class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        def possible(length):
            d = defaultdict(int)
            for i in range(length):
                d[s[i]] += 1
            if length - max(d.values()) <= k:
                return True
            for i in range(length, n):
                d[s[i]] += 1
                d[s[i - length]] -= 1
                if length - max(d.values()) <= k:
                    return True
            return False

        l = 1
        r = n
        ans = 1
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans