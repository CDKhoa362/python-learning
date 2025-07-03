class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = None

class ListNode:
    def  __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    
    def binary_to_decimal(self):
        result = 0
        cur = self.head
        while cur:
            result = result * 2 + cur.value
            cur = cur.next
        return result
        