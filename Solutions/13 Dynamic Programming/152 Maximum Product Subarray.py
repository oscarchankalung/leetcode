import math
from typing import List

class Attempt:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min = nums[0]
        prev_max = nums[0]
        best_max = nums[0]

        for num in nums[1:]:
            curr_min = min(prev_min * num, prev_max * num, num)
            curr_max = max(prev_max * num, prev_min * num, num)
            prev_min = curr_min
            prev_max = curr_max
            best_max = max(curr_max, best_max)

        return best_max

class Solution_Swap:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        best_max = -math.inf

        for num in nums:
            prev_min = curr_min
            prev_max = curr_max
            if num >= 0:
                curr_min = min(prev_min * num, num)
                curr_max = max(prev_max * num, num)
            if num < 0:
                curr_min = min(prev_max * num, num)
                curr_max = max(prev_min * num, num)
            best_max = max(best_max, curr_max)

        return best_max

class Solution_Bidirection:
    def maxProduct(self, nums: List[int]) -> int:
        prefix_max = 1
        suffix_max = 1
        best_max = -math.inf

        for i in range(len(nums)):
            prefix_max = (prefix_max or 1) * nums[i]
            suffix_max = (suffix_max or 1) * nums[~i]
            best_max = max(prefix_max, suffix_max, best_max)
            
        return best_max