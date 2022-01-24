from typing import List

class Attempt:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        if count == len(nums): return
        for i in range(count):
            nums.remove(0)
            nums.append(0)

class Solution:
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