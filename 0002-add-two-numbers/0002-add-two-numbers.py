# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1: 
                val += l1.val
                l1 = l1.next
            if l2: 
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return res.next
        