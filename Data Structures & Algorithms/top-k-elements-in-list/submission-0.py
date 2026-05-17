class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        occ = defaultdict(list)
        for i, j in freq.items():
            occ[j].append(i)
        op = []
        for i in range(len(nums), 0, -1):
            if occ[i]:
                for j in occ[i]:
                    op.append(j)
        return op[:k]