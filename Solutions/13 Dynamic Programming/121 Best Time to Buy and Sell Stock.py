import math
from typing import List

class Attempt:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

# tracking min_price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

# tracking min_price with tabulationma
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        dp = [0] * len(prices)

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price)
        return dp[-1]

# tracking cur_profit
class Solution_Kadane:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            cur_profit += prices[i] - prices[i-1]
            cur_profit = max(0, cur_profit)
            max_profit = max(max_profit, cur_profit)
        return max_profit

class Solution_State:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        hold = -math.inf
        
        for price in prices:
            best = max(best, hold + price)
            hold = max(hold, -price)
        return best