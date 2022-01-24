from typing import List

# recusrive brute force > time limit exceeded
class Attempt_Brute_Force:
    def rob(self, nums: List[int]) -> int:
        
        def recursive(i):
            if i >= len(nums):
                return 0
            return nums[i] + max(recursive(i+2), recursive(i+3))
        
        result = 0

        for i in range(2):
            result = max(result, recursive(i))
        return result

# dynamic programming
class Attempt_Tabulation:
    def rob(self, nums: List[int]) -> int:
        
        def recursive(i):
            if i >= len(nums):
                return 0
            if dp[i] == '':
                dp[i] = nums[i] + max(recursive(i+2), recursive(i+3))
            return dp[i]

        dp = [''] * len(nums)
        result = 0

        for i in range(2):
            result = max(result, recursive(i))
        return result

# recusrive brute force > time limit exceeded
class Solution_Brute_Force:
    def rob(self, nums: List[int]) -> int:
        def rob(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + rob(i+2), rob(i+1))
        return rob(0)

class Solution_Tabulation:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

class Solution_Optimized:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        cur = 0
        for num in nums:
            cur = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = cur
        return cur

#https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP