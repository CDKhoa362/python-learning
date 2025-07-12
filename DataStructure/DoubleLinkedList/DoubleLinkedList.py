class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None



class DoubleLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None: # There is not node in list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None    

        self.length -= 1
        return temp

    def pretend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """


        Returns:
            _type_: _description_
        """

        # Không có node
        if self.length == 0:
            return None
        temp = self.head
        # Có 1 nốt duy nhất
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Đã có nhiều node có sẵn
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self,index):
        """
        Retrieves the value of the node at the specified index.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Any or None: The value of the node if found, otherwise None.

        Description:
            - Returns None if:
                - index < 0
                - index >= length of the list
                - index is not an integer
            - If index is in the first half of the list, traversal starts from head.
            - If index is in the second half, traversal starts from tail.
        """
        if index < 0 or index >= self.length or not isinstance(index, int):
            return None
        temp = self.head
        if index < self.length / 2: 
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
        return temp.value
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        """
        Insert a new node at the specified index in the doubly linked list.
        Args:
            index (int): Vị trí chèn node mới
            value (any): Giá trị của node mới

        Returns:
            _bool_: True/False

        Description:
            1. Undesired scenario:
                - index < 0
                - index > The length of Double Linked List
            2. Additional scenario:
                - index = 0
                - index == The length of Double Linked List
            3. Besides:
                Insert into (Index: 2, Value: E) DLL
                None <=> A <=> B <=> [C] <=> D <=> None
                         0     1      2      3
                              Bef    Aft
                Bef <=> new_node <=> After
                3.1 We need to create two variables: before and after.
                Then, we will insert the new_node between them.
        """
        # 1
        if index < 0 or index > self.length:
            return False
        
        # 2
        if index == 0:
            return self.pretend(value)
        if index == self.length:
            return self.append(value)
        
        # 3.1
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        
        # 3.2
        new_node.prev = before
        new_node.next = after   

        before.next = new_node
        after.prev = new_node
        
        self.length += 1

        return True

    def remove(self, index):
        """
        Removes the node at the specified index from the doubly linked list.

        Args:
            index (int): The index of the node to be removed.

        Returns:
            Node or None: The removed node if successful, or None if the index is invalid.

        Description:
            1. Undesired scenarios:
                - index < 0
                - index >= length of the list
                - index is not an integer
            2. Edge cases:
                - index == 0 → remove from the beginning
                - index == length - 1 → remove from the end
            3. Standard case:
                - Remove node at the given index and re-link surrounding nodes

                Remove (Index: 2, Value: C) from DLL
                None <=> A <=> B <=> [C] <=> D <=> None
                         0     1      2      3
                              prev   temp   next
                Update the connection between B and D. 
                +  B = temp.prev
                => B.next  = temp.prev.next
                
                +  D = temp.next
                => D.prev = temp.next.prev

                Connect B <=> D, 
                temp.prev.next = temp.next (B -> D)
                temp.next.prev = temp.prev (B <- D)

        """
        if index < 0 or index > self.length or not isinstance(index, int):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.prev = None
        temp.next = None

        self.length -= 1
        return temp
    
    def reverse(self):

        if self.length <= 1:
            return self.head

        current = self.head
        new_head = None

        while current:
            current.prev, current.next = current.next, current.prev # Đảo ngược con trỏ prev, next
            new_head = current
            current = current.prev

        old_head = self.head
        self.head = new_head
        self.head.prev = None

        self.tail = old_head
        self.tail.next = None


    def partition_list(self, x):
        if self.length <= 1:
            return self.head
    
        # Node giả
        dummy1 = Node(0)
        dummy2 = Node(0)

        current1 = dummy1
        current2 = dummy2
        
        temp = self.head
        while temp:
            next_node = temp.next

            # Tách node đang đứng hiện tại ra khỏi danh sách gốc
            temp.next = None
            temp.prev = None

            # Phân loại Node
            if temp.value < x:
                
                # Nối node temp hiện tại vào current1 với Node < x
                current1.next = temp
                temp.prev = current1
                current1 = temp
            else:

                # Nối node temp hiện tại vào current2 với Node >= x
                current2.next = temp
                temp.prev = current2
                current2 = temp 
            
            # Di chuyển temp lên 1 bước ở danh sách gốc.
            temp = next_node

        # Ghép dummy1 vào dummy2 (cuối dummy1 vào đầu dummy2)
        current1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = current1

        # Cập nhật lại head
        self.head = dummy1.next
        if self.head:
            self.head.prev = None

            # Cập nhật lại tail (vì dummy2 có thể rỗng nên phải duyệt lại)
            temp = self.head
            while temp.next:
                temp = temp.next

            self.tail = temp
            self.tail.next = None

        return self.head

        




          


        

        




            




    
    


        
        




