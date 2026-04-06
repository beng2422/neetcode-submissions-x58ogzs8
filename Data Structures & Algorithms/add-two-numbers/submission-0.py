# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        newNode = ListNode(0)
        newNodePtr = newNode
        currNode = newNode
        prev = 0
        while l1 and l2:
            
            addition = (l1.val+l2.val)

            newNode = ListNode(addition%10 + prev)
            currNode.next = newNode
            prev = addition // 10
            print('prevVal', prev)
            currNode = currNode.next
            l1 = l1.next
            l2 = l2.next
        if prev==1:
            currNode.next = ListNode(prev)
        while l1:

            currNode.next = ListNode(l1.val)
            currNode = currNode.next
            l1 = l1.next
            
        while l2:

            currNode.next = ListNode(l2.val)
            currNode = currNode.next
            l2 = l2.next

        return newNodePtr.next
            