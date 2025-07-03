class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class ListNode:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1


    def reverse_between(self, start_index, end_index):

        # Điều kiện.
        if not isinstance(start_index, int) or not isinstance(end_index, int):
            return False
        
        if start_index < 0 or end_index < 0:
            return False
        
        if start_index >= self.length or end_index >= self.lengh:
            return False
        
        if start_index > end_index:
            start_index, end_index = end_index, start_index

        if start_index == end_index:
            return None
        
        dummy_node = Node(0)
        dummy_node.next = self.head

        prev = dummy_node
        # Di chuyển prev đến giá trị đầu tiên trong range (start_index, end_index)
        # prev thành node nằm phía trước (tay trái) các nodes cần đảo
        for _ in range(start_index):
            prev = prev.next
        
        current = prev.next
        # Đảo ngược các nodes nằm trong range(start_index, end_index)
        for _ in range(end_index - start_index):
            to_move = current.next # node dùng để di chuyển

            # Di chuyển node phải sang node trái
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

        # Thay đổi lại heading
        self.head = dummy_node.next
        return True
    



            

