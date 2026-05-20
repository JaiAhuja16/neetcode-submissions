import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        @functools.cache
        def recurse(floor):
            if floor <= 1:
                return cost[floor]
            return min(recurse(floor - 1) , recurse(floor - 2)) + cost[floor]
        return recurse(len(cost) - 1)