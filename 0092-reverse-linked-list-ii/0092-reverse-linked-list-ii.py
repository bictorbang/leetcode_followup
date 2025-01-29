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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head 
        res = ListNode(0, head)
        prev = res
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next   
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp     
        return res.next