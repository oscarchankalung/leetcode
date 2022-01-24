from typing import List

class Attempt:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        arr = []
        self.backtrack(s, arr, res)
        return res
        
    def backtrack(self, s, arr, res):
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            
            if left != left[::-1]:
                continue
            if left == left[::-1]:
                self.backtrack(right, arr + [left], res)
        
        if s == s[::-1]:
            res.append(arr + [s])

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        arr = []
        self.backtrack(s, arr, res)
        return res
        
    def backtrack(self, s, arr, res):
        if not s:
          res.append(arr)

        for i in range(1, len(s)+1):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]:
                self.backtrack(right, arr + [left], res)
