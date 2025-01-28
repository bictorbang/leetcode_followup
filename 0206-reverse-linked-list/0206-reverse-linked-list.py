# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = None
        while cur:
            ans = ListNode(val = cur.val, next = ans)
            cur = cur.next
        return ans