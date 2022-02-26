class Attempt:
    def reverseBits(self, n: int) -> int:
        n = format(n, '032b')
        return int(n[::-1], 2)

class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) ^ (n & 1)
            n >>= 1
        return res