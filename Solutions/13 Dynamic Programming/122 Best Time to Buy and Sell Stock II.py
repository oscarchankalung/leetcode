import math
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
        
        for i in range(1, len(prices)):
          if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(1, len(prices)):
            cur_profit = prices[i] - prices[i-1]
            cur_profit = max(cur_profit, 0)
            max_profit += cur_profit
        return max_profit

class Solution_State:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        hold = -math.inf
        
        for price in prices:
            best = max(best, hold + price)
            hold = max(hold, best - price)
        return best