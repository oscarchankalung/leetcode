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
  f[0] = 0
  f[1] = 1
  for i in range(2, n+1):
    f[i] = f[i-1] + f[i-2]
  return f[n]
```

## Reference

- [Blog - Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/)