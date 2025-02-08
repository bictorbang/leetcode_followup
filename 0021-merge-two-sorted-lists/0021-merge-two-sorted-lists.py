# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list1.val < list2.val:
            res = ListNode(0, list1)
            cur1 = list1.next
            cur2 = list2
        else:
            res = ListNode(0, list2)
            cur1 = list1
            cur2 = list2.next
        cur = res.next
        while 1:
            if not cur1:
                cur.next = cur2
                break
            if not cur2:
                cur.next = cur1
                break
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        return res.next