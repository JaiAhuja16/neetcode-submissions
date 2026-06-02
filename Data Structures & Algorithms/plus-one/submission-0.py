class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        while i >= 0 and digits[i] + 1 == 10:
            digits[i] = 0
            i -= 1
        if i == -1:
            return [1] + digits
        digits[i] += 1
        return digits
            