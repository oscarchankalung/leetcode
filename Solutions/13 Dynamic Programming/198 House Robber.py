from typing import List

# time limit exceeded
class Attempt_Recursive:
    def rob(self, nums: List[int]) -> int:

        def recursive(i):
            if i >= n:
                return 0
            return nums[i] + max(recursive(i+2), recursive(i+3))
        
        n = len(nums)
        return max(recursive(0), recursive(1))

class Attempt_Tabulation:
    def rob(self, nums: List[int]) -> int:
        
        def recursive(i):
            if i >= n:
                return 0
            if i not in dp:
                dp[i] = nums[i] + max(recursive(i+2), recursive(i+3))
            return dp[i]

        n = len(nums)
        dp = {}
        return max(recursive(0), recursive(1))

class Attempt_Iterative:    
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = {}
        
        for i in range(n):
            a = dp[i-3] if i-3 in dp else 0
            b = dp[i-2] if i-2 in dp else 0
            dp[i] = nums[i] + max(a, b)
        
        return max(dp[n-2], dp[n-1])

class Attempt_Optimized:    
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0,0,0,0]
        
        for i in range(n):
            dp[-1] = nums[i] + max(dp[0], dp[1])
            dp[0], dp[1], dp[2], dp[3] = dp[1], dp[2], dp[3], 0
            
        return max(dp[-3], dp[-2])

# time limit exceeded
class Solution_Recursive:
    def rob(self, nums: List[int]) -> int:
        def rob(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + rob(i+2), rob(i+1))
        return rob(0)

class Solution_Iterative:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

class Solution_Optimized:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for num in nums:
            prev2, prev1 = prev1, max(num + prev2, prev1)
        return prev1

# https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP