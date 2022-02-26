from typing import List

class Attempt:
    def missingNumber(self, nums: List[int]) -> int:
        correct_sum = sum(range(len(nums) + 1))
        missing_sum = sum(nums)
        return correct_sum - missing_sum


class Solution_SUM:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

class Solution_XOR:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

class Solution_Binary:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left