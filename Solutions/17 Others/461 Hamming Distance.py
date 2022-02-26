class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        n = x ^ y
        while n:
            n = n & (n - 1)
            res += 1
        return res

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')