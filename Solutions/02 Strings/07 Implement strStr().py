# substring
class Attempt:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if n == 0:
            return 0

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
            i += 1
        return -1

# brute force > time limit exceeded
class Attempt_Brute_Force:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if n == 0:
            return 0 

        for i in range(m - n + 1):
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
                if j == n - 1:
                    return i
        return -1

# KMP
class Solution_KMP:
    def strStr(self, haystack: str, needle: str):
        m = len(haystack)
        n = len(needle)

        if n == 0:
            return 0
        
        lps = self.getLPS(needle)
        i = 0
        j = 0

        while i < m:
            # check if haystack matches needle by char
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                # skip j and fix i if possible
                if j != 0:
                    j = lps[j-1]
                # increment i if cannot skip
                else:
                    i += 1
            # return index if finish looping needle
            if j == n:
                return i - j
        return -1

    def getLPS(self, needle: str):
        n = len(needle)
        lps = [0]*n
        length = 0
        i = 1

        while i < n:
            if needle[length] == needle[i]:
                length += 1
                lps[i] = length
                i += 1
            # fix i and see example: "AAACAAA"
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

# python find
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)