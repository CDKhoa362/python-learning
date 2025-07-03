class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = None

class ListNode:
    def __init__(self,value):
        new_node = Node(value, next)
        self.head = new_node
        self.length = 1



    # Cách 1
    def remove_duplicates(self):

        cur = self.head
        while cur:
            run = cur
            while run.next:
                if run.next.value == cur.value:
                    run.next = run.next.next.next
                    self.length -= 1
                else:
                    run = run.next
            cur = cur.next
        return cur



    