from typing import List

class Attempt:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i+1]:
                buy = i+1
            elif prices[i] < prices[i+1]:
                sell = i+1
            if buy < sell:
                profit += prices[sell] - prices[buy]
                buy = i+1
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
          if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
        return profit