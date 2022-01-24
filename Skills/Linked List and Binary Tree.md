# Skill: Linked List and Binary Tree

## Linked List Syntax

- Use `zero = ListNode(0, head)` to remember the head of linked list
- Use `return zero.next` to return the head of modified linked list

## Binary Tree Syntax

- Use `queue = deque([root])` and `node = queue.popleft()` for BFS
- Use `stack = [root]` and `node = stack.pop()` for DFS

## Binary Tree Methodology

- Breadth First Traversalclass Solution:
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
        while i < m:
            nums1[k] = nums3[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
            
- Depth First Traversal
  - In Order Traversal (Left-Root-Right)
  - Pre Order Traversal (Root-Left-Right)
  - Post Order Traversal (Left-Right-Root)

## Reference

- [Blog - Difference between BPS and DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
- [Blog - BPS and DFS for Binary Tree](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)
- [Blog - Maximum Depth of Binary Tree](https://christinalalay.medium.com/crack-leetcode-140-maximum-depth-of-binary-tree-91a963d10a9a)