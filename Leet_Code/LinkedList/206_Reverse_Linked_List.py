class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        prev = None

        while current:
            after = current.next
            current.next = prev # Đảo ngược con trỏ
            
            prev = current # Di chuyển prev 1 bước
            current = after # Di chuyển current 1 bước
        
        return prev


            

