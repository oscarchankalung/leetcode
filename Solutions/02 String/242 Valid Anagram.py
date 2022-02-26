from collections import Counter

class Attempt:
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

class Solution:
  def isAnagram(self, s, t):
      dic_s, dic_t = {}, {}
      for char in s:
          dic_s[char] = dic_s.get(char, 0) + 1
      for char in t:
          dic_t[char] = dic_t.get(char, 0) + 1
      return dic_s == dic_t