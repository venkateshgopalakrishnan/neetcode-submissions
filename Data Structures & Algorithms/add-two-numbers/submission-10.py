# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import floor
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        ans_pointer = ans_head = None
        carry = 0
        while pointer1 or pointer2:
            val1, val2 = 0 if not pointer1 else pointer1.val, 0 if not pointer2 else pointer2.val
            num_sum, carry = (val1 + val2 + carry) % 10, floor((val1 + val2 + carry) / 10)
            if not ans_pointer:
                ans_pointer = ListNode(val = num_sum)
                ans_head = ans_pointer
            else:
                ans_pointer.next = ListNode(val = num_sum)
                ans_pointer = ans_pointer.next
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
        if carry:
            ans_pointer.next = ListNode(val = carry)
        return ans_head
