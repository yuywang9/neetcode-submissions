class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        slow, fast = 0, 0
        while fast < len(prices):
            while prices[fast] < prices[slow]:
                slow += 1
            res = prices[fast] - prices[slow]
            profit = max(res, profit)
            fast += 1
        return profit