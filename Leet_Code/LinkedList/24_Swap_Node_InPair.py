# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy_node = ListNode(0)
        dummy_node.next = head
        prev = dummy_node

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # swap node
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        head = dummy_node.next
        return head













        