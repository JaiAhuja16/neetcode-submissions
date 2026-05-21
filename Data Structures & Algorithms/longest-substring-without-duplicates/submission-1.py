class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        st = set()
        maxi = 0
        n = len(s)
        while r < n:
            while l < r and s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            maxi = max(maxi, r - l + 1)
            r += 1
        return maxi