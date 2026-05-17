class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            a = s[l].lower()
            b = s[r].lower()
            if a.isalnum() and b.isalnum():
                if a == b:
                    l += 1
                    r -= 1
                else:
                    return False
            elif a.isalnum():
                r -= 1
            else:
                l += 1
        return True