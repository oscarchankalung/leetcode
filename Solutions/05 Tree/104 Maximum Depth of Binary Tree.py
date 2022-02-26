from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Attempt:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left and root.right:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        elif root.left:
            return 1 + self.maxDepth(root.left)
        elif root.right:
            return 1 + self.maxDepth(root.right)
        else:
            return 1

# recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# iterative: breath-first-search with queue (first-in-first-out)
class Solution_BPS():
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)]) if root else []
        depth = 0
        
        while queue:
            node, depth = queue.popleft()
            if node.left:
              queue.append((node.left, depth + 1))
            if node.right:
              queue.append((node.right, depth + 1))
            
        return depth

# iterative: depth-first-search with stack (last-in-last-out)
class Solution_DFS():
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)] if root else []
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        
        return max_depth