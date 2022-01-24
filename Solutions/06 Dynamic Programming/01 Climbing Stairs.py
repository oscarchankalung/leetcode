class Attempt:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        while n > 0:
            current = first + second
            first = second
            second = current
            n -= 1
        return second

class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        while n > 0:
            first, second = second, first + second
            n -= 1
        return second

# time limit exceeded
class Solution_Recursive:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return 3
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution_Dict:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[1] = 1
        cache[2] = 2
        
        if n in cache:
            return cache[n]
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
        
class Solution_Array:
    def climbStairs(self, n: int) -> int:
        array = [0, 1]
        while n > 0:
            current = array[0] + array[1]
            array[0] = array[1]
            array[1] = current
            n -= 1
        return array[1]