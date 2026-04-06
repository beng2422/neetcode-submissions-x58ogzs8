# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy1 = ListNode(0, head)
        dummy = dummy1
        second = dummy1
        if n == 1 and head.next == None:
            head = None
            return head

        for _ in range(n):
            dummy = dummy.next
        while dummy and dummy.next:
            dummy = dummy.next
            second = second.next
        if second.next:
            val = second.next.next
        else:
            val = None
        second.next = val

        return dummy1.next

