from typing import List

class Attempt:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = []
        for r in range(9):        # 000000000/111111111/222222222 > 333333333
            for c in range(9):    # 012345678/012345678/012345678 > 012345678
                i = r // 3        # 000000000/000000000/000000000 > 111111111
                j = c // 3        # 000111222/000111222/000111222 > 000111222
                a = r % 3         # 000000000/111111111/222222222 > 000000000
                b = c % 3         # 012012012/012012012/012012012 > 012012012
                box_c = i * 3 + j # 000111222/000111222/000111222 > 333444555
                box_r = a * 3 + b # 012012012/345345345/678678678 > 012012012
                
                row = board[r][c]
                col = board[c][r]
                box = board[box_c][box_r]
                
                if row in rows or col in cols or box in boxes:
                    return False
                else:
                    if row != '.': rows.append(row)
                    if col != '.': cols.append(col)
                    if box != '.': boxes.append(box)
            rows = []
            cols = []
            boxes = []
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [[] for _ in range(N)]
        cols = [[] for _ in range(N)]
        boxes = [[] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                b = (c // 3) + (r // 3) * 3 # 000111222/000111222/000111222 > 333444555
                val = board[r][c]
                if val == '.': continue
                if val in rows[r]: return False
                if val in cols[c]: return False
                if val in boxes[b]: return False
                rows[r].append(val)
                cols[c].append(val)
                boxes[b].append(val)
        return True