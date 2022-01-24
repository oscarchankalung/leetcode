from typing import List

class Attempt:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        while i < len(nums1) and i < len(nums2):
            if nums1[i] == nums2[i]:
                i += 1
            elif nums1[i] < nums2[i]:
                nums1.pop(i)
            elif nums1[i] > nums2[i]:
                nums2.pop(i)
        if len(nums1) < len(nums2):
            return nums1
        else:
            return nums2
                

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        intersect = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
        return intersect