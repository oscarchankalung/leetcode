import random
from typing import List

class Attempt:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        result = self.original[:]
        random.shuffle(result)
        return result

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.array = list(self.original)

    def reset(self) -> List[int]:
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            j = random.randrange(i+1)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array