class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        op = []
        curr = 0
        i = 0
        n = len(s)
        while i < n:
            curr = 1
            freq[s[i]] -= 1
            if freq[s[i]] > 0:
                st = set(s[i])
                i += 1
                while i < n and any(freq[j] > 0 for j in st):
                    st.add(s[i])
                    freq[s[i]] -= 1
                    i += 1
                    curr += 1
            else:
                i += 1
            op.append(curr)
        return op