# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        def addDigits(l1, l2, res, carry = 0):
            if not l1 and not l2 and not carry:
                return res
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val
            res.next = ListNode(s := (l1_val + l2_val + carry))
            carry = 1 if s > 9 else 0
            res.next.val %= 10
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None
            addDigits(l1_next, l2_next, res.next, carry)
        addDigits(l1, l2, res)
        return res.next
        