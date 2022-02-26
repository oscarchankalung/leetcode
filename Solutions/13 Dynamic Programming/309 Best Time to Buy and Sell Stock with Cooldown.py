from typing import List
import math

class Attempt:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        max_profits = [0] * n
        
        s = 0
        slow_profit = 0
        min_price = prices[0]
        
        for i in range(1, n):
            
            kadane = prices[i] - prices[i-1]
            
            if kadane > 0:
                
                curr_profit = max(0, prices[i] - min_price)
                curr_profit += max_profits[s-2] if s-2 >= 0 else 0
                slow_profit = max(slow_profit, curr_profit)
                
                fast_profit = kadane
                fast_profit += max_profits[i-3] if i-3 >= 0 else 0

                if fast_profit > slow_profit:
                    s, slow_profit, min_price = i-1, fast_profit, prices[i-1]
                    max_profits[i] = fast_profit
                else:
                    max_profits[i] = slow_profit
            
            else:
                
                max_profits[i] = max_profits[i-1]
                    
            i += 1
        
        return max_profits[-1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sell, cool = -math.inf, 0, 0
        
        for price in prices:
            prev_hold, prev_sell, prev_cool = hold, sell, cool
            
            hold = max(prev_hold, prev_cool - price)
            sell = prev_hold + price
            cool = max(prev_cool, prev_sell)
        
        return max(cool, sell)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/761981/PythonGo-O(n)-by-DP-and-state-machine.-w-Visualization