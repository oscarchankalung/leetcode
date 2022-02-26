class Attempt:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        array = list(str(abs(x)))
        array.reverse()
        x = int(''.join(c for c in array))
        return x * sign if x < 2 ** 31 - 1 else 0

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x_reverse = int(str(abs(x))[::-1]) * sign
        return x_reverse if pow(-2, 31) <= x_reverse <= pow(2, 31) - 1 else 0