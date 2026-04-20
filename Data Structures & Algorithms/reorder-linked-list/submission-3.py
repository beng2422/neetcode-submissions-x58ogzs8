# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first count, then reverse then put them togethor
        if not head.next:
            return 
        def printL(node):
            while node:
                print(node.val)
                node = node.next
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        #reverse 2nd half
        curr = head
        for i in range(count //2):
            prev = curr
            curr = curr.next
        prev.next = None
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        #put them togethor
        curr = head
        while prev:
            nextCurr = curr.next
            curr.next = prev
            curr = curr.next
            prev = nextCurr
       # return head

















         