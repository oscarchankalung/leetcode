from typing import List

class Attempt:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        i = 0
        j = 0
        k = 0
        
        while i < m and j < n:
            if nums3[i] < nums2[j]:
                nums1[k] = nums3[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        if i < m:
            nums1[k:] = nums3[i:]
        if j < n:
            nums1[k:] = nums2[j:]

class Solution_Back:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n:
            if m and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
class Solution_Sort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:]
        nums1.sort()