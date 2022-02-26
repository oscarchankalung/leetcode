from typing import List

class Attempt:
    def rotate(self, matrix: List[List[int]]) -> None:
        copy = [row[:] for row in matrix]
        N = len(matrix)
        for r in range(N):     # 000 > 111 > 222
            for c in range(N): # 012 > 012 > 012
                i = N - r - 1  # 222 > 111 > 000
                matrix[c][i] = copy[r][c]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        N = len(matrix)
        for r in range(N-1):        # 000 > 11 > 2
            for c in range(r+1, N): # 123 > 23 > 3
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]