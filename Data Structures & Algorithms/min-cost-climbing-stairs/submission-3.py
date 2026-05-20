# import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        # @functools.cache
        # def recurse(floor):
        #     if floor <= 1:
        #         return cost[floor]
        #     return min(recurse(floor - 1) , recurse(floor - 2)) + cost[floor]
        # return recurse(len(cost) - 1)
        for i in range(n - 2, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1]) 