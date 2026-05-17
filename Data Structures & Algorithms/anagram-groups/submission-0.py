class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            tup = [0] * 26
            for j in i:
                tup[ord(j) - 97] += 1
            groups[tuple(tup)].append(i)
        return list(groups.values())