from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Attempt:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
  
        while curr:
            prev = ListNode(curr.val, prev)
            curr = curr.next
        return prev
        
# iterative
class Solution_Iterative:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            n = curr.next    #[2,3,4,5]
            curr.next = prev #[1,None]
            prev = curr      #[1,None]
            curr = n         #[2,3,4,5]
        return prev

# recursive
class Solution_Recursive:
    def reverseList(self, head):
        return self.reverse(head)

    def reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)