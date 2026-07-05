class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(f"{len(string)}#{string}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        length = len(s)
        while index < length:
            index2 = index
            while index2 < length and s[index2].isnumeric():
                index2 += 1
            substrLength = int(s[index : index2])
            decoded.append(s[index2 + 1 : index2 + substrLength + 1])
            index = index2 + substrLength + 1
        return decoded