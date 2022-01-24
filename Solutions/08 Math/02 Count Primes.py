class Solution_Readable:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0
        i = 2

        while i * i < n:
            if primes[i] == 1:
                for j in range(i*i, n, i):
                    primes[j] = 0
            i += 1
            
        return sum(primes)

class Solution_Fast:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i] == 1:
                primes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
            
        return sum(primes)

class Solution_Fastest:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [1]*(n//2)

        for i in range(3, int(n**.5)+1, 2):
            if primes[i//2]:
                primes[i*i//2::i] = [0]*((n - i*i - 1)//(2*i) + 1)
                
        return sum(primes)