from collections import Counter

class Attempt:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
                