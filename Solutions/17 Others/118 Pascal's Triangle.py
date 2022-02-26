from tkinter import N
from typing import List
import math

class Attempt:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        
        for r in range(1, numRows):
            prevRow = rows[r-1]
            currRow = [1]
            loopMid = math.ceil((r+1)/2)
            halfMid = math.floor((r+1)/2)
            
            for c in range(1, loopMid):
                currRow.append(prevRow[c-1] + prevRow[c])
            
            halfRow = currRow[:halfMid]
            halfRow.reverse()
            currRow = currRow + halfRow
            rows.append(currRow)
                
        return rows

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for r in range(1, numRows):
            rows.append([1] * (r+1))
            for c in range(1, r):
                rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
        return rows