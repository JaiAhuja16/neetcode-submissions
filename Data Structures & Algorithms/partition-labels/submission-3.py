class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [-1] * 26
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
        op = []
        i = 0
        n = len(s)
        while i < n:
            l = 1
            gotill = last[ord(s[i]) - 97]
            i += 1
            while i <= gotill:
                gotill = max(gotill, last[ord(s[i]) - 97])
                i += 1
                l += 1
            op.append(l)
        return op