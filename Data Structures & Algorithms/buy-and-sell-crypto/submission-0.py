class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = float('inf')
        for i in prices:
            profit = max(profit, i - mini)
            mini = min(mini, i)
        return profit