from typing import List

class Attempt:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            pop = nums.pop(len(nums) - 1)
            nums.insert(0, pop)

class Attempt:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]