# Algorithm: Knuth-Morris-Pratt (KMP)

- **Degenerating property**: pattern with subpatterns appearing more than once
- **Knuth-Morris-Pratt**: use of degenerating property to improve pattern searching
- **Worst case complexity** from `O(n*m)` in naive to `O(n)`
- **Longest proper prefix which is also suffix (LPS)**: see example in reference

## Implementation

- `getLPS()`
- `searchPattern()`

## Examples

- [x] 028 Implement strStr()

## Reference

- [LeetCode - Discussion of Implement strStr()](https://leetcode.com/problems/implement-strstr/discuss/12956/C%2B%2B-Brute-Force-and-KMP)
- [Blog - KMP in plain](http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/)
- [Blog - KMP in pattern searching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)