class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i
        op = []
        i = 0
        n = len(s)
        while i < n:
            l = 1
            gotill = last[s[i]]
            i += 1
            while i <= gotill:
                gotill = max(gotill, last[s[i]])
                i += 1
                l += 1
            op.append(l)
        return op