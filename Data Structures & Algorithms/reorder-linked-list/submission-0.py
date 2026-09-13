# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point of linked list
        pointer1 = pointer2 = head
        while pointer2:
            if pointer2.next:
                if pointer2.next.next:
                    pointer1, pointer2 = pointer1.next, pointer2.next.next
                    continue
            break
        # reverse the second half
        mid_start = pointer1
        pointer1 = pointer1.next
        mid_start.next = prev = None
        while pointer1:
            temp = pointer1.next
            pointer1.next = prev
            prev = pointer1
            pointer1 = temp
        # insert reversed second half in the first half
        pointer1 = head
        current = prev
        while current:
            temp1 = pointer1.next
            temp2 = current.next
            pointer1.next = current
            current.next = temp1
            current = temp2
            pointer1 = temp1
        

            