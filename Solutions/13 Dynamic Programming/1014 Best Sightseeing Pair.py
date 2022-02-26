from typing import List

# case_1 = [9, 9, 1, 1, 1, 1, 1]
# case_2 = [9, 1, 1, 9, 1, 1, 1]
# case_3 = [1, 1, 1, 9, 1, 1, 9]
# case_4 = [1, 1, 1, 1, 1, 9, 9]

# case_5 = [9, 1, 1, 9, 1, 1, 9]
# case_6 = [9, 1, 1, 1, 1, 1, 9]

# i       = [  0,  1,  2,  3,  4]
# values  = [  8,  1,  5,  2,  6]
# score_i = [  8,  2,  7,  5,  0]
# score_j = [  0,  0,  3, -1,  2]
# score_m = [  0 , 8, 11, 11, 11]

# i       = [  0,  1,  2,  3,  4,  5,  6,  7,  8]
# values  = [  6,  3,  7,  4,  7,  6,  6,  4,  9]
# score_i = [  6,  4,  9,  7, 11, 11, 12, 11,  0]
# score_j = [  0,  2,  5,  1,  3,  1,  0, -3,  1]
# score_m = [  0,  8, 11, 10, 12, 12, 12, 12, 13]

class Attempt_Recursive:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_score = 0
        
        for i in range(n):
            start = i + 1
            end = min(n, i + values[i] + 1)
            for j in range(start, end):
                score = values[i] + values[j] + i - j
                max_score = max(max_score, score)
        return max_score

class Attempt_Dynamic:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score_i = 0
        max_score = 0

        for i in range(len(values)-1):
            j = i + 1
            cur_score_i = values[i] + i
            cur_score_j = values[j] - j
            max_score_i = max(max_score_i, cur_score_i)
            max_score = max(max_score, max_score_i + cur_score_j)
        return max_score

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_i = 0
        best = 0

        for j, value in enumerate(values):
            best = max(best, best_i + value - j)
            best_i = max(best_i, value + j)
        return best