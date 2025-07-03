from typing import Optional

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class ListNode:
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = None
        self.length = 1

    def Reverse_Between(self, first_index: int, second_index: int):
        
        # Kiểm tra input
        if (not isinstance(first_index, int)) or (not isinstance(second_index, int)):
            return False
        if first_index < 0 and second_index < 0:
            return False
        if (first_index >= self.length) or (second_index >= self.length):
            return False
        
        if first_index > second_index:
            temp = first_index
            first_index = second_index
            second_index = temp
        else:
            dummy = ListNode(0)
            prev = dummy
            

