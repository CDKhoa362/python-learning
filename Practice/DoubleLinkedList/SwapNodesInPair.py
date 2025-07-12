class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # swap
            first.next = second.next
            second.prev = first.prev

            if second.next:
                second.next.prev = first

            second.next = prev.next
            prev.next = second

            # Di chuyển prev lên first
            prev = first
        
        self.head = dummy.next
        if self.head:
            self.head.prev = None
        return self.head
            


            
