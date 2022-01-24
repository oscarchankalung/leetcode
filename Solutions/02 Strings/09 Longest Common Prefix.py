from typing import List

class Attempt:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        char = ''
        for i in range(0, len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                try:
                    if strs[j][i] != char:
                        return res
                except IndexError:
                    return res
            res += char
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest