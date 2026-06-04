class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        def f(i, j):
            if i == m:
                return j == n or (set(p[j + 1:]) == {'*'})
            if j == n:
                return i == m
            if j < n - 1 and p[j + 1] == '*':
                return f(i, j + 2) or ((p[j] == '.' or s[i] == p[j]) and f(i + 1, j))
            if p[j] == '.' or s[i] == p[j]:
                return f(i + 1, j + 1)
            return False
        
        return f(0, 0)