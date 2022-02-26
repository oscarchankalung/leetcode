# Skill: Dynamic Programming

- Dynamic Programming is mainly an optimization over recursion
- Any recursive solution that has repeated calls for the same inputs can be optimized.
- The idea is to store the result of sub-problems, so that we do not have to re-compute them.
- This optimization reduces time complecities from exponential to polynomial.

## Implementation

```
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
```
def fibonacci(n: int) -> int:
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
```

## Methodology

- Step
  - Recursion: use the result of sub-problem as next recursion's input
  - Tabulation: store the result of sub-problem in array instead
  - Iteration: use the result of sub-problem stored in array instead
  - Optmization: store the result of sub-problem as pointers instead

- Design
  - Memorization: decide what to store, input, result or goal
  - Direction: iterate array using top-down or bottom-up approach

## Reference

- [Blog - Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/)