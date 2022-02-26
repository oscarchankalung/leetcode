from typing import List

class Solution_Recursive:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def recursive(i):
            if i < 0:
                return 0
            if i < 2:
                return cost[i]
            return cost[i] + min(recursive(i-1), recursive(i-2))
        
        n = len(cost)
        return min(recursive(n-1), recursive(n-2))

class Solution_Tabulation:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def recursive(i):
            if i < 0:
                return 0
            if i < 2:
                return cost[i]
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(recursive(i-1), recursive(i-2))
            return dp[i]
        
        dp = {}
        n = len(cost)
        return min(recursive(n-1), recursive(n-2))

class Solution_Iterative:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        n = len(cost)

        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])

class Solution_Optimized:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        
        for i in range(2, len(cost)):
            first, second = second, cost[i] + min(first, second)

        return min(first, second)