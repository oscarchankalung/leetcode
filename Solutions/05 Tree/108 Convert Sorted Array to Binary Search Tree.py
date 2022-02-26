from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        half = len(nums) // 2
        node = TreeNode(nums[half])
        node.left = self.sortedArrayToBST(nums[:half])
        node.right = self.sortedArrayToBST(nums[half+1:])
        return node

class Solution_2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recursive(left, right):
            if left > right:
                return None
            half = (left + right) // 2
            node = TreeNode(nums[half])
            node.left = recursive(left, half - 1)
            node.right = recursive(half + 1, right)
            return node
        
        return recursive(0, len(nums) - 1)