import math
from typing import List

# time limit exceeded
class Attempt:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maxSubarray(i):
            max_sum = -math.inf
            cur_sum = -math.inf
            
            for _ in range(n):
                num = nums[i%n]
                cur_sum += num
                cur_sum = max(cur_sum, num)
                max_sum = max(max_sum, cur_sum)
                i += 1
            return max_sum

        n = len(nums)
        max_sum = -math.inf
        for i in range(n):
            cur_sum = maxSubarray(i)
            max_sum = max(max_sum, cur_sum)
        return max_sum

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = best_max = -math.inf
        curr_min = best_min = math.inf
        s = 0
        
        for num in nums:
            curr_max = max(curr_max + num, num)
            best_max = max(curr_max, best_max)
            curr_min = min(curr_min + num, num)
            best_min = min(curr_min, best_min)
            s += num
        
        if best_min == s:
            return best_max
        return max(best_max, s - best_min)

# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/635487/Python-Kadane's-solution
