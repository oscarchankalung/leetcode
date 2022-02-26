from typing import List

class Attempt:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid] :
                right = mid
            else:
                left = mid + 1
        return -1