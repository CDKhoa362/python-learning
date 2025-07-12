from typing import Optional
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = None

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """_summary_

        Args:
            head (Optional[ListNode]): _description_
            x (int): _description_

        Returns:
            Optional[ListNode]: _description_
        """

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1 = dummy1
        prev2 = dummy2

        temp = head
        while temp:
            next_node = temp.next
            temp.next = None    
            if temp.val < x:
                prev1.next = temp
                prev1 = prev1.next
            else:
                prev2.next = temp
                prev2 = prev2.next
            temp = next_node
        prev1.next = dummy2.next
        head = dummy1.next

        return head











