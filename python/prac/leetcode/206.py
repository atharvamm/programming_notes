# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_ptr,cur_ptr = None, head
        while cur_ptr is not None:
            temp = cur_ptr.next
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = temp
        return prev_ptr