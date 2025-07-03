from typing import Optional
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = None

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """_summary_

        Args:
            head (Optional[ListNode]): _description_
            x (int): _description_

        Returns:
            Optional[ListNode]: _description_
        """

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1 = dummy1
        prev2 = dummy2

        temp = head
        while temp:
            next_node = temp.next
            temp.next = None
            if temp.val < x:
                prev1.next = temp
                prev1 = prev1.next
            else:
                prev2.next = temp
                prev2 = prev2.next
            temp = next_node
        prev1.next = dummy2.next
        head = dummy1.next

        return head



import random
from typing import Optional


def check_num_in_array(A: Optional[list], size: int, n: int) -> bool:
    if A is None or size == 0:
        return False
    return n in A


def use_check_num_in_array():
    size = random.randint(1,100)
    A = [random.randint(1, 99) for _ in range(size)]
    for i in range(100):
        print(i, check_num_in_array(A, size, i))


def improve_using_check_num_in_array():
    size = random.randint(1,100)
    A = [random.randint(1, 99) for _ in range(size)]
    set_a = set(A)
    for i in range(100):
        print(i, check_num_in_array(set_a, size, i))


import re
raw_names = ["Nguyễn  vAn Thanh", " trần   thị Nhung", "Huỳnh Thúc Điền.", "“Lê van  NaM”"]

def clean_name(name):
    # Xóa ký tự đặc biệt và chuẩn hóa khoảng trắng
    name = re.sub(r'[^\w\s]', '', name, flags=re.UNICODE).strip()
    # Viết hoa chữ cái đầu mỗi từ
    return ' '.join(word.capitalize() for word in name.split())

for name in raw_names:
    print(clean_name(name))













