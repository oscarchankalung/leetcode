class Attempt:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''
        for char in s:
            if char.isalnum():
                alnum += char.lower()
        return alnum == alnum[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        return s == s[::-1]