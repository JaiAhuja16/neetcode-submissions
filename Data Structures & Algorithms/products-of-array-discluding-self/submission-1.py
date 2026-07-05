class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * (n + 1)
        suffixProd = [1] * (n + 1)
        for i in range(n):
            prefixProd[i + 1] = prefixProd[i] * nums[i]
            suffixProd[n - i - 1] = suffixProd[n - i] * nums[n - i - 1]
        for i in range(n):
            nums[i] = prefixProd[i] * suffixProd[i + 1]
        return nums