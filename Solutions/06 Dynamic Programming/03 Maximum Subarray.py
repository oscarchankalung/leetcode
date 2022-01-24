import math
from typing import List

class Attempt:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = -math.inf

        for num in nums:
            cur_sum += num
            cur_sum = max(cur_sum, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

# brute force > time limit exceeded
class Solution_Brute_Force:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
        return max_sum

# dynamic programming
class Solution_Tabulation:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[0] is cur_sums
        # dp[1] is max_sums
        dp = [[0]*len(nums) for i in range(2)]

        for i in range(len(nums)):
            dp[0][i] = max(dp[0][i-1] + nums[i], nums[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i])
        return dp[1][-1]

# https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer