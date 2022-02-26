from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        curr_min = 0
        curr_max = 0
        best_max = 0
        
        for num in nums:
            prev_min = curr_min
            prev_max = curr_max
            if num == 0:
                curr_min = 0
                curr_max = 0
            elif num > 0:
                curr_min = prev_min + 1 if prev_min else 0 # [1,-1,1]
                curr_max = prev_max + 1                    # [1,1,1]
            elif num < 0:
                curr_min = prev_max + 1                    # [-1,-1,-1]
                curr_max = prev_min + 1 if prev_min else 0 # [1,-1,-1]
            best_max = max(best_max, curr_max)
        
        return best_max