class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def is_palindrome(self):

        if self.length == 0 or self.length == 1:
            return True
        
        left = self.head
        right = self.tail

        while left != right and left.prev != right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev

        return True


        

        