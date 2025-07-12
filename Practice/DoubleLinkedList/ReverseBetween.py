class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def reverse_between(self, start_index, end_index):
        if not isinstance(start_index, int) or not isinstance(end_index, int):
            return False
        if start_index < 0 or end_index < 0:
            return False
        if start_index >= self.length or end_index >= self.length:
            return False
        if start_index > end_index:
            start_index, end_index = end_index, start_index
        if start_index == end_index:
            return self.head
        
        dummy = Node(0)
        dummy.next = self.head
        left = dummy

        # Di chuyển prev đến vị trí trước node đầu tiên trong ds các node cần đảo
        for _ in range(start_index):
            left = left.next

        # Node đầu tiên trong ds node cần đảo
        mid = left.next
        for _ in range(end_index - start_index):
                right = mid.next
                # Gỡ right ra khỏi danh sách.
                mid.next = right.next
                if right.next:
                    right.next.prev = mid
                # Chèn right trước sau left
                right.next = left.next
                left.next.prev = right
                left.next = right
                right.prev = left

        self.head = dummy.next
        self.head.prev = None

        return self.head

                
                



                    

                        

        
        
        

        
