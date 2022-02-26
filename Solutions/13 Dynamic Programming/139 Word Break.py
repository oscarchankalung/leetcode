# "applepenapple"
# ["apple", "pen"]
# "cars"
# ["car", "ca", "rs"]
# "cbca"
# ["bc","ca"]
# "catsandog"
# ["cats", "dog", "sand", "and", "cat", "an"]

from typing import List

# time limit exceeded
class Attempt_Recursive:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
            
        for word in wordDict:
            n = len(word)
            if word == s[:n] and self.wordBreak(s[n:], wordDict):
                return True
        return False

class Solution_Recursive:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def recursive(m: int):
            if m == n: return True
                
            for i in range(m,n):
                substring = s[m:i+1]
                if substring in wordDict and recursive(i+1):
                    return True
            return False
        
        wordDict = set(wordDict)
        n = len(s)
        return recursive(0)

class Solution_Tabulation:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def recursive(m: int):
            if m == n: return True
            if m in dp: return dp[m]
                
            for i in range(m,n):
                substring = s[m:i+1]
                if substring in wordDict and recursive(i+1):
                    dp[m] = True
                    return True
            dp[m] = False
            return False
        
        wordDict = set(wordDict)
        n = len(s)
        dp = {}
        return recursive(0)

class Solution_Iterative:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = {}

        for m in range(n):
            for i in range(m,n):
                substring = s[m:i+1]
                if substring in wordDict:
                    dp[m] = dp[i+1]
            dp[m] = False
        

        return dp[0]