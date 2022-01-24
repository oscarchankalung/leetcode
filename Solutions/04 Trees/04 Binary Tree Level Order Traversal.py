from typing import List, Optional
from collections import deque
from xml.etree.ElementInclude import LimitedRecursiveIncludeError

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Attempt:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([[root]]) if root else []
        values = [[root.val]] if root else []
        
        while queue:
            level = queue.popleft()
            next_queue = []
            next_values = []
            
            for node in level:
                if node.left:
                    next_queue.append(node.left)
                    next_values.append(node.left.val)
                if node.right:
                    next_queue.append(node.right)
                    next_values.append(node.right.val)
            
            if len(next_queue) > 0:
                queue.append(next_queue)
            if len(next_values) > 0:
                values.append(next_values)
                
        return values

class Solution_Iterative:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = [root] if root else []
        values = [] if root else []
        
        while level:
            next_level = []
            curr_values = []
            
            for node in level:
                curr_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            level = next_level
            values.append(curr_values)
                
        return values

class Solution_Recursive:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverse(level, values) -> List[List[int]]:
            if not level:
                return values

            next_level = []
            curr_values = []

            for node in level:
                curr_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            values.append(curr_values)
            return traverse(next_level, values)
        
        return traverse([root] if root else [], [])
