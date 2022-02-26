from typing import List

class Attempt:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        if count == len(nums): return
        for _ in range(count):
            nums.remove(0)
            nums.append(0)

class Solution_Pop_Append:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        zeros = []
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeros.append(0)
            else:
                i += 1
        nums += zeros

class Solution_Two_Pointers:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            if nums[slow] != 0:
                slow += 1