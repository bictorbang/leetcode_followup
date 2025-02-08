# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        cur = head
        hashmap = set()
        while cur.next:
            if cur.next in hashmap:
                return True
            hashmap.add(cur.next)
            cur = cur.next
        return False
