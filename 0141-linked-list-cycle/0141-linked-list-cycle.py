# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        hashmap = defaultdict()
        while cur:
            if cur in hashmap:
                return True
            hashmap[cur] = cur.next
            cur = cur.next
        return False
