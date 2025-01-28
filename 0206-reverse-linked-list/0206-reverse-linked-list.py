# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, cur, prev):
            if not cur:
                return prev
            next_ = cur.next
            cur.next = prev
            prev = cur
            return self.rev(next_, prev)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(head, None)