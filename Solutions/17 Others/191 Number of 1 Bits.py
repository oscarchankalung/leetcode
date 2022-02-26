class Attempt:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for d in bin(n):
            if d == '1':
                res += 1
        return res

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res