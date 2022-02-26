import math
from typing import List

class Attempt:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -math.inf
        sell = 0
        best = 0
        
        for price in prices:
            prev_hold, prev_sell, prev_best = hold, sell, best
            
            hold = max(prev_hold, prev_best - price)
            sell = prev_hold + price - fee
            best = max(prev_best, sell)
        
        return best

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        best = 0
        hold = -math.inf
        
        for price in prices:
            best = max(best, hold + price - fee)
            hold = max(hold, best - price)
        return best