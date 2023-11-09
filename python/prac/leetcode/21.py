
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_ptr,next_ptr = None,None
        head = None
        while any([list1,list2]):
            if list1 is None:
                next_ptr = list2
                list2 = list2.next
            elif list2 is None:
                next_ptr = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    next_ptr = list1
                    list1 = list1.next
                elif list2.val < list1.val:
                    next_ptr = list2
                    list2 = list2.next
            if head is None:
               head = next_ptr
               cur_ptr = head
            else:
                cur_ptr.next = next_ptr
                cur_ptr = next_ptr
        return head


