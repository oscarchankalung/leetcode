from typing import List
from copy import deepcopy
from collections import Counter

# time limit exceeded
class Attempt_Recursive:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        def deleteAndEarn(count):
            max_point = 0
            cur_point = 0
            for num in list(count):
                num_point = num * count[num]
                copy = deepcopy(count)
                del copy[num]
                del copy[num-1]
                del copy[num+1]
                cur_point = num_point + deleteAndEarn(copy)
                max_point = max(max_point, cur_point)
            return max_point
        
        count = Counter(nums)
        return deleteAndEarn(count)

class Attempt_Iterative:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        nums = list(count)
        
        if len(count) == 1:
            num = nums[0]
            return num * count[num]
        
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            prev1 = dp[i-1] if 0 <= i-1 and nums[i-1] < num-1 else 0
            prev2 = dp[i-2] if 0 <= i-1 and nums[i-2] < num-1 else 0
            prev3 = dp[i-3] if 0 <= i-2 and nums[i-3] < num-1 else 0
            dp[i] = max(prev1, prev2, prev3) + num * count[num]
        return max(dp[-2], dp[-1])

class Attempt_Two_Pointers:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        prev2 = 0
        prev1 = 0
        for num in range(min(nums), max(nums)+1):
            prev2, prev1 = prev1, max(prev1, prev2 + num * count[num])
        return prev1

class Solution_House_Robber:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        count = Counter(nums)
        end = max(nums) + 1
        dp = [0] * end

        for i in range(end):
            dp[i] = max(i * count[i] + dp[i-2], dp[i-1])
        return dp[-1]

class Solution_Native:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        prev = None
        avoid = 0
        using = 0
        for num in sorted(count):
            if num-1 != prev:
                avoid, using = max(avoid, using), num * count[num] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), num * count[num] + avoid
            prev = num
        return max(avoid, using)