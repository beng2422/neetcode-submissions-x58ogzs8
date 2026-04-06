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



        while curr:
            curr = curr.next
            size+=1
        
        #first case - if we remove the first value of the list (n==size)
        curr = head
        if n==size:
            return head.next
        
        if n==1:
            for i in range(size-2):
                curr = curr.next
            print(curr.val)
            curr.next = None
            return head



        for i in range( size-n-1):
            head = head.next
        head.next = head.next.next
        return curr