# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
        

            temp=head.next
            head1 = head
            head.next = prev
            prev = head1
            head = temp


        return prev

# 1, 2, 3





# prev = 1
# head = 2
# head.next = prev
