class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return -1

        # slightly optimal
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     left, right = 0, n - 1
        #     currTarget = target - nums[i]
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if nums[mid] == currTarget and mid != i:
        #             return [i, mid]
        #         elif nums[mid] < currTarget:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return -1

        # best
        n = len(nums)
        complement = {}
        for i in range(n):
            if target - nums[i] in complement:
                return [complement[target - nums[i]], i]
            complement[nums[i]] = i
        return -1