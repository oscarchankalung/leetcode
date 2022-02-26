from tkinter import N


class Attempt:
    def fib(self, n: int) -> int:
        fibonacci = [0, 1]
        while n > 1:
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
            n -= 1
        return fibonacci[-1] if n == 1 else 0

class Solution_Recursive:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-2) + self.fib(n-1)

class Solution_Swap:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for _ in range(n):
            a,b = b, a+b
        return a

class Solution_Dynamic:
    def fib(self, n: int) -> int:
        if n == 0: return 0 
        memo = (0, 1)
        for _ in range(2, n+1):
            memo = (memo[-1], memo[-2] + memo[-1])
        return memo[-1]