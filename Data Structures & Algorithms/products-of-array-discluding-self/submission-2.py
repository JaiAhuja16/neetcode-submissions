class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefProd = 1
        for i in range(n):
            output[i] = prefProd
            prefProd *= nums[i]
        suffProd = nums[-1]
        for i in range(n - 2, -1, -1):
            output[i] *= suffProd
            suffProd *= nums[i]
        return output