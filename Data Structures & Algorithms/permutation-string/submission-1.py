class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26
        for i in range(n):
            freq_s1[ord(s1[i]) - 97] += 1
            freq_s2[ord(s2[i]) - 97] += 1

        same = 0
        for i in range(26):
            same += int(freq_s1[i] == freq_s2[i])

        if same == 26:
            return True

        for i in range(n, len(s2)):
            ind1 = ord(s2[i]) - 97
            ind2 = ord(s2[i - n]) - 97

            if freq_s1[ind1] == freq_s2[ind1]: 
                same -= 1
            if freq_s1[ind2] == freq_s2[ind2]: 
                same -= 1

            freq_s2[ind1] += 1
            freq_s2[ind2] -= 1

            if freq_s1[ind1] == freq_s2[ind1]:
                same += 1
            if freq_s1[ind2] == freq_s2[ind2]:
                same += 1
            
            if same == 26:
                return True
        return same == 26