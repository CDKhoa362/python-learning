# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not isinstance(left, int) or not isinstance(right, int):
            return False

        if left < 0 and right < 0:
            return False
            
        if left > right:
            left, right = right, left

        if left == right:
            return head


        dummy_node = ListNode(0)
        dummy_node.next = head


        prev = dummy_node

        for _ in range(left-1):
            prev = prev.next
        
        current = prev.next
        for _ in range(right - left):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
        return dummy_node.next
        