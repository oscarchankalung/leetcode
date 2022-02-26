from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Attempt:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        plusOne = 0
        node = ListNode()
        head = node
        
        while l1 or l2 or plusOne:
            node_sum = plusOne
            if l1 and l2:
                node_sum += l1.val + l2.val
            elif l1:
                node_sum += l1.val
            elif l2:
                node_sum += l2.val
            if node_sum > 9:
                node.next = ListNode(node_sum % 10)
                plusOne = 1
            else:
                node.next = ListNode(node_sum)
                plusOne = 0
            node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return head.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = ListNode()
        head = node
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            val = val1 + val2 + carry
        
            node.next = ListNode(val % 10)
            carry = val // 10
            node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return head.next