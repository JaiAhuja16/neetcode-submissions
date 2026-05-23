class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        set_t = set(t)

        if m > n:
            return ""

        freq_s = [0] * 128
        freq_t = [0] * 128
        for i in range(m):
            freq_s[ord(s[i]) - 97] += 1
            freq_t[ord(t[i]) - 97] += 1

        def check(freqA, freqB):
            for i in set_t:
                if freqA[ord(i) - 97] < freqB[ord(i) - 97]:
                    return False
            return True

        l = 0
        left = 0
        right = n + 1
        if check(freq_s, freq_t):
            left = 0
            right = m - 1

        for r in range(m, n):
            freq_s[ord(s[r]) - 97] += 1
            if not check(freq_s, freq_t):
                continue
            if r - l < right - left:
                left = l
                right = r
            # print(l, r)
            while r - l + 1 >= m:
                freq_s[ord(s[l]) - 97] -= 1
                if check(freq_s, freq_t):
                    # print(l, r, 1)
                    l += 1
                    if r - l < right - left:
                        left = l
                        right = r
                else:
                    freq_s[ord(s[l]) - 97] += 1
                    break
        return s[left:right + 1] if right - left < n else ""