from typing import List

# Testcase
[0]
[0,2,3]
[1,1,1,1,4]
[2,3,1,1,4]
[3,2,1,0,4]
[3,0,8,2,0,0,1]
[5,9,3,2,1,0,2,3,3,1,0,0]

# Dynamic Programming
# True or False
# Furthest Index / Closest Goal

# time limit exceeded
class Attempt_Recusrive:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        for i, num in enumerate(nums):
            if i+num >= n-1:
                return True
            else:
                for j in range(1, num+1):
                    if self.canJump(nums[i+j:]):
                        return True
                return False

class Attempt_Iterative:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        
        i = n-1
        dp = [False] * n
        while i > -1:
            num = nums[i]
            if i+num >= n-1:
                dp[i] = True
            else:
                for j in range(1, num+1):
                    if dp[i+j]:
                        dp[i] = True
                        break
            i -= 1
        return dp[0]

class Attempt_Optimized:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        
        max_jump = 0
        for i, num in enumerate(nums[:-1]):
            max_jump = max(max_jump, i + num)
            if max_jump <= i: return False
        return True

class Solution_Furthest_Index:
    def canJump(self, nums: List[int]) -> bool:       
        max_index = 0
        for i, num in enumerate(nums):
            if max_index < i: return False
            max_index = max(max_index, i + num)
        return True

class Solution_Closest_Goal:
    def canJump(self, nums: List[int]) -> bool:       
        n = len(nums)
        min_goal = n-1
        for i in range(n)[::-1]:
            if i + nums[i] > min_goal:
                min_goal = i
        return min_goal == 0