from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Attempt:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, None, None)] if root else []
        
        while stack:
            node, lower, upper = stack.pop()
            if lower is not None and lower >= node.val:
                return False
            if upper is not None and upper <= node.val:
                return False
            if node.right:
                stack.append((node.right, node.val, upper))
            if node.left:
                stack.append((node.left, lower, node.val))
                
        return True

# recursive traversal with valid range
class Solution_Recursive:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, lower=-math.inf, upper=math.inf) -> bool:
            if not node:
                return True
            if lower >= node.val or node.val >= upper:
                return False
            else:
                return (validate(node.right, node.val, upper) and 
                    validate(node.left, lower, node.val))
        
        return validate(root)

# iterative traversal with valid range
class Solution_Iterative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)] if root else []
        
        while stack:
            node, lower, upper = stack.pop()
            val = node.val
            if lower >= val or val >= upper:
                return False
            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))
                
        return True

# recursive inorder traversal 
class Solution_Recursive_Inorder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(node) -> bool:
            if not node:
                return True
            if not inorder(node.left):
                return False
            if self.prev >= node.val:
                return False
            self.prev = node.val
            return inorder(node.right)
        
        self.prev = -math.inf
        return inorder(root)

# iterative inorder traversal 
class Solution_Iterative_Inorder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = -math.inf

        while stack or root:
            # traverse left first
            while root:
                stack.append(root)
                root = root.left
            # validate value
            node = stack.pop()
            if prev >= node.val:
                return False
            prev = node.val
            # traverse right afterwward
            root = root.right

        return True
