from typing import Optional
from Collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_Recursive:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(left, right) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return (symmetric(left.left, right.right) and 
                    symmetric(left.right, right.left))

        return symmetric(root.left, root.right)

class Solution_Iterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root.left, root.right)]) if root else []

        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                queue.append((left.right, right.left))
                queue.append((left.left, right.right))
            
        return True