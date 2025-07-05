class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = None

class ListNode:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
    
    
    def swap_pairs(self):

        #   | Description:                                      |
        #   | - Swaps adjacent pairs of nodes in a singly linked|
        #   |   list by modifying the next pointers.            |
        #   |                                                   |
        #   | Parameters:                                       |
        #   | - None: Operates on the linked list's head.       |
        #   |                                                   |
        #   | Return:                                           |
        #   | - None: Modifies the linked list in place.        |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - If the list is empty or has one node, no swaps  |
        #   |   are performed.                                  |
        #   | - For each pair of adjacent nodes, swaps their    |
        #   |   positions by updating the next pointers.        |
        #   | - Uses a dummy node to simplify handling of the   |
        #   |   head node swap.                                 |
        #   | - Iterates through the list using a first pointer,|
        #   |   keeping the head unchanged until the final      |
        #   |   update.                                         |
        #   | - Sets the head to the new first node at the end. |
        #   +===================================================+
        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Swap Node
            first.next = second.next
            second.next = first
            prev.next = second

            # Move Prev -> First (First is now the second node in the swapped pair)
            prev = first

        self.head = dummy_node.next



