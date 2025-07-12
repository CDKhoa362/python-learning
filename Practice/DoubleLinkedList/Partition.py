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


            

        


         






        


        

