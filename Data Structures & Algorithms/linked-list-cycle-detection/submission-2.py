# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Use two pointers- if one pointer is twice as fast as the other pointer we get the correct answer - they 
        #will eventually hit each other in O(2n)?
        pointer2 = head.next
        while head and pointer2:
            if pointer2 == head:
                return True
            pointer2 = pointer2.next
            if pointer2:
                pointer2 = pointer2.next
            head = head.next
        return False










        # #I am not sure how to do this in O(1) space - I could make a set and check if it reached 
        # visited = set()
        # while head:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False
