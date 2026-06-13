from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @lru_cache
        def f(index):
            if index >= n:
                return 1
            if s[index] == '0':
                return 0
            return f(index + 1) + (f(index + 2) if index < n - 1 and int(s[index] + s[index + 1]) <= 26 else 0)
        return f(0)