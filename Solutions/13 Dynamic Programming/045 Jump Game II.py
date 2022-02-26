
from typing import List

# Testcase
[0] #0
[1,1,1,1,4] #4
[2,3,1,1,4] #2
[3,0,8,2,0,0,1] #2
[5,9,3,2,1,0,2,3,3,1,0,0] #3
[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3] #2

i              = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14]
nums           = [ 7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
this_max_index = [ 7, 1,11, 9,13,11, 7,14,17, 9,11,13,21,13,17]
prev_max_index = [ 0, 7, 7, 7, 7, 7, 7, 7,14,14,14,14,14,14,14]
curr_max_index = [ 7, 7,11,11,13,13,13,14,17,17,17,17,21,21,21]
min_jump       = [ 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

class Attempt:
    def jump(self, nums: List[int]) -> int:        
        prev_max_index = 0
        curr_max_index = 0
        min_jump = 0
    
        for i, num in enumerate(nums):
            if prev_max_index < i:
                min_jump += 1
                prev_max_index = curr_max_index
            curr_max_index = max(curr_max_index, i + num)
        return min_jump

class Solution_Recursive:
    def jump(self, nums: List[int], i: int = 0) -> int:
        n = len(nums)
        if i >= n - 1: return 0
        if i + nums[i] >= n - 1: return 1

        min_jump = n - 1
        for j in range(1, nums[i]+1):
            min_jump = min(min_jump, 1 + self.jump(nums, i+j))

        return min_jump

class Solution_Tabulation:
    def jump(self, nums: List[int]) -> int:
        def jump(nums, i):
            if i + nums[i] >= n - 1: return 1
            if i in dp: return dp[i]

            dp[i] = n - 1
            for j in range(1, nums[i]+1):
                dp[i] = min(dp[i], 1 + jump(nums, i+j))
            return dp[i]
        
        n = len(nums)
        dp = {}
        if n == 1: return 0

        return jump(nums, 0)

class Solution_Iterative:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        if n == 1: return 0

        for i in range(n)[::-1]:
            if i + nums[i] >= n - 1:
                dp[i] = 1
            else:
                dp[i] = n - 1
                for j in range(1, nums[i]+1):
                    dp[i] = min(dp[i], 1 + dp[i+j])

        return dp[0]