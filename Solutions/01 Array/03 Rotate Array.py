from typing import List

class Attempt:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            pop = nums.pop(len(nums) - 1)
            nums.insert(0, pop)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]