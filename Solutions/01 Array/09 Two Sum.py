from typing import List

class Attempt:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            try:
                value = target - nums[i]
                index = nums.index(value, i + 1)
                return [i, index]
            except ValueError:
                continue

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            if num in hashMap:
                return [hashMap[num], i]
            else:
                hashMap[target - num] = i