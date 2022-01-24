from typing import List

class Attempt:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 5 == 0:
                res.append('Buzz')
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i))
        return res

class Solution_String:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):

            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            res_i = ''

            if divisible_by_3:
                res_i += 'Fizz'
            if divisible_by_5:
                res_i += 'Buzz'
            if not res_i:
                res_i += str(i)

            res.append(res_i)
        return res

class Solution_Hash:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        hash_dict = { 3: 'Fizz', 5: 'Buzz' }

        for i in range(1, n+1):
            res_i = ''
            for divisible, string in hash_dict.items():
                if i % divisible == 0:
                    res_i += string
            if not res_i:
                res_i += str(i)
            res.append(res_i)
        return res