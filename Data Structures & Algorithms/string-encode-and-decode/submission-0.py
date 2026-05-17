class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join((str(len(i)) + "$" + i for i in strs))

    def decode(self, s: str) -> List[str]:
        op = []
        n = len(s)
        i = 0
        while i < n:
            l = ""
            while i < n and s[i].isnumeric():
                l += s[i]
                i += 1
            l = int(l)
            op.append(s[i + 1 : i + l + 1])
            i += l + 1
        return op