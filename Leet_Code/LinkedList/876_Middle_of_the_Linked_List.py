from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = None
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        