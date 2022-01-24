# Algorithm: Binary Search

## Implementation

```
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

- Correctly initialize the boundary variables `left` and `right` by including all possible elements
- Decide return value as `left` or `left - 1`? After exiting the while loop, left is the minimal value satisfying the condition function;
- Design the `condition` function. This is the most difficult and beautiful part that needs lots of practice.

## Examples

- [x] 278 First Bad Version
- [ ] 069 Sqrt(x)
- [ ] 035 Search Insert Position
- [ ] 410 Split Array Largest Sum
- [ ] 875 Koko Eating Bananas

## Reference

- [LeetCode - Discussion of First Bad Version](https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.)