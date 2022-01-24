from typing import List

class Attempt:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(str(digit) for digit in digits)
        return list(str(int(string) + 1))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits