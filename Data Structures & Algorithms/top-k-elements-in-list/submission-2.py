class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for ele in nums:
            freq[ele] = freq.get(ele, 0) + 1
        freqToEle = {}
        for ele, count in freq.items():
            if count in freqToEle:
                freqToEle[count].append(ele)
            else:
                freqToEle[count] = [ele]
        mostFreq = []
        c = 0
        for count in range(len(nums), 0, -1):
            if count in freqToEle:
                mostFreq.extend(freqToEle[count])
        return mostFreq[:k]