# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #just add up each val until its done and then reverse the output
        #handle the case where sum goes over

        head = l1
        carry = 0
        end_of_head = None
        while l1 and l2:

            sumVal = l1.val + l2.val + carry
            l1.val = sumVal%10
            
            carry = sumVal//10 if sumVal//10 else 0
            if not l1.next or not l2.next:
                end_of_head = l1
            l1 = l1.next
            l2 = l2.next
        


        #cases:
        #carry exists or carry doesnt exist
        #if it exists- what happens when l1 exists or l2 exists?

        #
            
        #3 cases: l2 still exists and carry doesnt. l2 exists and carry does, l2 doesnt exist and carry does

        if l2:
            end_of_head.next = l2
        while end_of_head and end_of_head.next and carry:

            sumVal = end_of_head.next.val + carry
            end_of_head.next.val = sumVal%10
            end_of_head = end_of_head.next
            
            carry = sumVal//10 if sumVal//10 else 0

        if carry:
            end_of_head.next = ListNode(carry)
        return head

        # if l2 and carry:
        #     new_end = None
        #     while l2:
        #         sumVal = l2.val + carry
        #         l2.val = sumVal%10
        #         if not l2.next:
        #             new_end = l2
        #         l2 = l2.next
                
        #         carry = sumVal//10 if sumVal//10 else 0
        #     end_of_head.next = l2
        #     end_of_head = new_end
        # elif l2:
        #     end_of_head.next = l2
        #     while l2.next:
        #         l2 = l2.next
        #     end_of_head = l2
        # if l1 and carry:
        #     while l1:
        #         sumVal = l1.val + carry
        #         l1.val = sumVal%10
        #         carry = sumVal//10 if sumVal//10 else 0
        #         if not l1.next:
        #             end_of_head = l1
        #         l1 = l1.next
        # if carry:
        #     end_of_head.next = ListNode(carry)




        
        #reverse l1 by just adding it to the string
        ret = ''










