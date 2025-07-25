class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    def reverse(self):
        if self.length <= 1:
            return self.head
    
        current = self.head
        new_head = None
    
        while current:
            current.prev, current.next = current.next, current.prev
            new_head = current
            current = current.prev
    
        old_head = self.head
        self.head = new_head
        self.head.prev = None
    
        self.tail = old_head
        self.tail.next = None


    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1 <-> 2 <-> 3 <-> 4 <-> 5
    
    DLL after reverse():
    5 <-> 4 <-> 3 <-> 2 <-> 1

"""

