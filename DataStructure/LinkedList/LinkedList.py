class Node:
    """
    Mô tả:
        Đại diện cho một Node trong Linked List
    Thuộc tính:
        value(any): Giá trị được lưu trữ trong node.
        next (Node | none): pointer trỏ tới Node tiếp theo.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Mô tả:
        Linked List là một cấu trúc dữ liệu với các đặc điểm:
            LL là một danh sách không có chỉ mục.
            Giá trị của các node trong LL có thể nằm bất kỳ đâu trong bộ nhớ (không nằm liền kề nhau như List)
            Đi từ Head đến Tail, giá trị cuối cùng của con trỏ(tail) bằng None

    Thuộc tính:
        new_node = Đại diện cho một node trong danh sách liên kết
        head: Con trỏ đến node đầu tiên trong danh sách liên kết
        tail: Con trỏ đến node cuối cùng trong danh sách liên kết
        length: Độ dài của danh sách liên kết.
    """
    
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
        """
            Mô tả O(1):
                Thêm node mới vào cuối danh sách liên kết.
            Tham số:
                value: Giá trị sẽ được lưu trữ trong node mới.
            Trường hợp:
                #1 Head và tail đều bằng None
                    + Tạo một node mới mà cả head và tail đều trỏ tới node đó.
                #2 Danh sách đã có sẵn nodes
                    + Cập nhật tail.next đến node cuối cùng(value) 
                    + Cập nhật lại tail để nó trỏ tới node mới, vì value vừa được cập nhật là node cuối cùng
            Kiểu trả về:
                bool
        """
        new_node = Node(value)
        if self.head is None: #1
            self.head = new_node
            self.tail = new_node
        else: #2
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
            Mô tả O(n):
                Xóa phần tử cuối cùng trong danh sách liên kết.
            Tham số:
                pre: node hiện tại.
                temp: node di chuyển tiếp theo
            Trường hợp:
                #1 Danh sách liên kết rỗng
                    + Return None
                #2 Danh sách liên kết chỉ có một node.
                    + Nếu sau khi xóa phần tử cuối cùng, mà độ dài danh sách liên kết = 0, thì đặt lại head, tail = None
                #3 Danh sách liên kết có nhiều node sẵn.
                    + Tạo 1 biến pre để lưu trữ node trước của temp đi qua
                    + Xóa phần tử bằng cách cập nhật tail bằng pre (tail.next = None)
                Kiểu trả về:
                    value (any)
        """
        if self.length == 0: #1
            return None

        #====================== #3 =========================
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre 
        self.tail.next = None
        self.length -= 1
        #===================================================

        if self.length == 0: #2
            self.head = None
            self.tail = None
        return temp.value

    def pretend(self, value):
        """
            Mô tả O(1):
                Thêm 1 node mới vào đầu danh sách.
            Tham số:
                value: node đầu tiên muốn cập nhật.
            Kiểu trả về:
                bool
            Trường hợp:
                #1 Danh sách liên kết không có phần tử.
                    head và tail bằng new_node
                #2 Danh sách liên kết có nhiều phần tử.
                    Di chuyển con trỏ của new_node đến head hiện tại (head khi chưa thêm node mới)
                    Cập nhật head bằng node vừa thêm.

        """
        new_node = Node(value)
        if self.length == 0: #1
            self.head = new_node
            self.tail = new_node
        else: #2
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        """
            Mô tả O(1):
                Xóa phần tử đầu tiên của danh sách liên kết.
            Kiểu trả về:
                value(any)
            Trường hợp:
                #1 Danh sách liên kết không có node.
                #2 Danh sách liên kết đã có sẵn nodes
                #3 Danh sách liên kết chỉ có 1 node duy nhất, sau khi xóa danh sách liên kết không có node
    
        """

        if self.length == 0: #1
            return None
        
        #====================== #2 =========================
        temp = self.head
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        #===================================================
        
        if self.length == 0: #3
            self.tail = None
        return temp
    
    def get(self, index):
        """
            Mô tả:
                Lấy giá trị của node dựa vào chỉ mục.
            Tham số:
                index(int)
            Kiểu giá về:
                value(any)
            Trường hợp:
                #1 index < 0
                #2 index >= self.length
                #3 type(index) != int
        """
        if index < 0 or index >= self.length:
            return None
        if not isinstance(index, int): #1,2,3
            return False
        temp = self.head 
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def change_value(self, index, value):
        """
            Mô tả:
                Thay đổi giá trị của node theo index.

            Tham số:
                index(int): index truy cập tới node
                value(any): giá trị thay đổi 

            Kiểu trả về:
                bool
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
            Mô tả:
                Thêm node vào danh sách liên kết ở vị trí index.

            Tham số:
                index(int): index truy cập tới node
                value(any): giá trị thay đổi
            Trường hợp:
                #0 index < 0 or index >= self.length or isinstance(index, int)
                #1 index == 0
                    ppretend
                #2 index = self.length
                    append

                #3 Danh sách liên kết đã có sẵn nodes
        """
        if index < 0 or index > self.length or not isinstance(index, int): #0
            return False
    
        if index == 0: #1
            return self.pretend(value)
        if index == self.length: #2
            return self.append(value)
        

        #====================== #3 =========================
        new_node = Node(value) 
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        #==================================================

        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if not isinstance(index, int):
            return False
        
        if index ==  0:
            return self.pop_first()
        
        if index == (self.length - 1):
            return self.pop()
        
        
        pre = self.get(index - 1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):

        """
            Mô tả:
                Đảo ngược danh sách liên kết đơn hiện tại.
                Sau khi thực hiện, node đầu tiên trở thành node cuối cùng và ngược lại.
            
            Cách hoạt động:
                - Đảo chiều con trỏ `next` của từng node trong danh sách.
                - Hoán đổi vị trí giữa `head` và `tail`.
                - Sử dụng ba biến tạm: `before`, `temp`, và `after` để duyệt qua danh sách và cập nhật liên kết.
            
            Trả về:
                None
        """
        # Đảo ngược tail và head
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None

        for _ in range(self.length):

            after = temp.next
            temp.next = before

            # move before -> temp, temp-> after
            before = temp
            temp = after

    def reverse_between(self, start_index, end_index):
        
        if not isinstance(start_index, int) or not isinstance(end_index, int):
            return False
        if start_index < 0 or end_index < 0:
            return False
        if start_index >= self.length or end_index >= self.length:
            return False
        if start_index == end_index:
            return None
        if start_index > end_index:
            start_index, end_index = end_index, start_index

        dummy_node = Node(0)
        dummy_node.next = self.head
        
        prev = dummy_node
        for _ in range(start_index):
            prev = prev.next

        current = prev.next
        for _ in range(end_index - start_index):
            to_move = current.next
            
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
        
        # Cập nhật lại head
        self.head = dummy_node.next
        
        # Cập lại tail
        new_tail = self.head
        while new_tail and new_tail.next:
            new_tail = new_tail.next
        self.tail = new_tail
        
        return True




        
        



    def find_middle_node(self):
        """
            Find and return the middle node of the singly linked list.

            Returns:
                _ListNode_: The middle node of the linked list.

            Description:
                1. Technique:
                    - Use two pointers: fast and slow.
                    - fast moves 2 steps at a time.
                    - slow moves 1 step at a time.
                2. When fast reaches the end, slow will be at the middle.
                3. Special cases:
                    - If the list has even number of nodes, it returns the second middle.
                    - If the list is empty (head is None), it returns None.
        """
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def has_loop(self):
        """
            Detect whether the singly linked list contains a cycle (loop).

            Returns:
                _bool_: True if there is a loop, False otherwise.

            Description:
                1. Technique:
                    - Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare).
                    - Use two pointers: fast and slow.
                    - fast moves 2 steps at a time.
                    - slow moves 1 step at a time.
                2. If fast and slow meet at any point, a cycle exists.
                3. If fast reaches the end (None), the list has no loop.
                4. Time Complexity: O(n)
                5. Space Complexity: O(1)
        """
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
      
    def find_kth_from_end(ll, k):
        
        slow = ll.head
        fast = ll.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )