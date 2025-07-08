# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        # Bước 1: Tìm middle node (slow dừng ở giữa)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Bước 2: Đảo ngược nửa sau danh sách
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Bước 3: So sánh 2 nửa
        left = head
        right = prev  # đầu của nửa sau đã đảo ngược
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
        
        """
        # Cách này chạy chậm (tạo singly linked list giả, sau khi đảo ngược ll gốc, rồi so sánh)
        reverse_head = None
        current = head
        while current:
            new_node = ListNode(current.val)
            new_node.next = reverse_head
            reverse_head = new_node

            # di chuyển
            current = current.next
        
        current = head
        while current:
            if current.val != reverse_head.val:
                return False
            current = current.next
            reverse_head = reverse_head.next

        return True
        """

        
    



        

        

        


            



        















        



        

        

        

        





        