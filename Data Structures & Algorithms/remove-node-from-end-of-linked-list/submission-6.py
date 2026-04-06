# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        if head is None:
            return head
        if head.next is None: 
            return head.next
        while curr:
            curr = curr.next
            size+=1
        curr = head
        for i in range( size-n-1):
            head = head.next
        if not head.next:
            head = None
        else:
            head.next = head.next.next
        return curr