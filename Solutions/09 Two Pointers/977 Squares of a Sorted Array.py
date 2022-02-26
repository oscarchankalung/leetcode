from collections import deque
from typing import List

class Attempt:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums

class Solution_Deque:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque([])
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left < right:
                res.appendleft(right ** 2)
                r -= 1
            else:
                res.appendleft(left ** 2)
                l += 1
        return list(res)

class Solution_List:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left < right:
                res[r-l] = right ** 2
                r -= 1
            else:
                res[r-l] = left ** 2
                l += 1
        return res