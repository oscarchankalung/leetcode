class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        prev = 0
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for c in s[::-1]:
            curr = roman_dict[c]
            if curr >= prev:
                res += curr
            else:
                res -= curr
            prev = curr
        return res