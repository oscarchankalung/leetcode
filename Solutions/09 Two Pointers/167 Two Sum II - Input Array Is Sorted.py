import enum
from typing import List

class Attempt:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        
        while i < len(numbers):
            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                elif numbers[i] == numbers[j]:
                    i += 1
                    j += 1
                elif numbers[i] + numbers[j] < target:
                    j += 1
                else:
                    break
            i += 1
            j = i + 1

class Solution_Hash_Table:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, num in enumerate(numbers):
            if num in hashTable:
                return [hashTable[num]+1, i+1]
            else:
                hashTable[target-num] = i

class Solution_Two_Pointers:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            elif s < target:
                i += 1
            elif s > target:
                j += 1

class Solution_Binary_Search:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers)
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            left, right = i + 1, last
            while left < right:
                mid = left + (right - left) // 2
                s = numbers[i] + numbers[mid]
                if s == target:
                    return [i+1, mid+1]
                elif s > target:
                    right = mid
                else:
                    left = mid + 1
            last = left
