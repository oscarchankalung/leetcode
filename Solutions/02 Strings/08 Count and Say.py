from itertools import groupby

class Attempt:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            s = self.countAndSay(n-1)
            length = len(s)
            say = ''
            last = s[0]
            count = 1
            for i in range(1, length):
                if last == s[i]:
                    count += 1
                else:
                    say += str(count) + last
                    last = s[i]
                    count = 1
                if i == length - 1:
                    say += str(count) + last
            return say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n-1) + '#'
            say = ''
            count = 1
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:
                    count += 1
                else:
                    say += str(count) + s[i]
                    count = 1
            return say

# python groupby
class Solution_Groupby:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n-1):
            say = ''
            for key, group in groupby(result):
                say += str(len(list(group))) + key
            result = say
        return result