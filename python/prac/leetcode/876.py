'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        list_form = []
        temp = head
        while True:
            list_form.append(temp.val)
            temp = temp.next
            if temp is None:
                break
        
        mid_ele = len(list_form)//2
        # print(list_form,mid_ele)
        
        temp_answer = head
        count = 0
        while True:
            if temp_answer.val == list_form[mid_ele]:
                count += 1
                answer = temp_answer
                if count == 2 :
                    break
            if temp_answer.next is None:
                break
            temp_answer = temp_answer.next
        return answer