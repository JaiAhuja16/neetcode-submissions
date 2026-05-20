# import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        # @functools.cache
        # def recurse(floor):
        #     if floor <= 1:
        #         return cost[floor]
        #     return min(recurse(floor - 1) , recurse(floor - 2)) + cost[floor]
        # return recurse(len(cost) - 1)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]