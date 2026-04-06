# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#next val=pointer of prev
#0,1,2,3
#1,0,2,3
        prev = None
        curr = head
        i = 0
        while curr:
            
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            print(head.val)

            # i+=1
            # if i>5:
            #     break
            

            # head = head.next
            # head = prev
            # prev = head.next

            
        return prev



