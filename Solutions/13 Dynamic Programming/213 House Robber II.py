from typing import List

class Attempt_Tabulation:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 3:
            return max(nums)
        
        def house0(i):
            if i >= n - 1:
                return 0
            return max(nums[i] + house0(i+2), house0(i+1))
        
        def house1(i):
            if i >= n:
                return 0
            return max(nums[i] + house1(i+2), house1(i+1))
        
        return max(house0(0), house1(1))

class Attempt_Tabulation:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = {}
        dp1 = {}
        
        if n <= 3:
            return max(nums)
        
        def house0(i):
            if i >= n-1:
                return 0
            if i not in dp0:
                dp0[i] = max(nums[i] + house0(i+2), house0(i+1))
            return dp0[i]
        
        def house1(i):
            if i >= n:
                return 0
            if i not in dp1:
                dp1[i] = max(nums[i] + house1(i+2), house1(i+1))
            return dp1[i]
        
        return max(house0(0), house1(1))

class Attempt_Iterative:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = {}
        dp1 = {}
        
        if n <= 3:
            return max(nums)
        
        for i in range(0,n-1):
            prev2 = dp0[i-2] if i-2 in dp0 else 0
            prev1 = dp0[i-1] if i-1 in dp0 else 0
            dp0[i] = max(nums[i] + prev2, prev1)
        
        for i in range(1,n):
            prev2 = dp1[i-2] if i-2 in dp1 else 0
            prev1 = dp1[i-1] if i-1 in dp1 else 0
            dp1[i] = max(nums[i] + prev2, prev1)
            
        return max(dp0[n-2], dp1[n-1])

class Attempt_Optimized:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = [0,0,0]
        dp1 = [0,0,0]
        
        if n <= 3:
            return max(nums)
        
        for i in range(0,n-1):
            dp0[2] = max(nums[i] + dp0[0], dp0[1])
            dp0[0], dp0[1] = dp0[1], dp0[2]
        
        for i in range(1,n):
            dp1[2] = max(nums[i] + dp1[0], dp1[1])
            dp1[0], dp1[1] = dp1[1], dp1[2]
            
        return max(dp0[-1], dp1[-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        def rob(x, y):
            prev2 = 0
            prev1 = 0
            for i in range(x,y):
                prev2, prev1 = prev1, max(nums[i] + prev2, prev1)
            return prev2
            
        return max(rob(0,n-1), rob(1,n))