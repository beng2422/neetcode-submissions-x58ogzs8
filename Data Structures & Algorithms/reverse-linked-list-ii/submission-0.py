# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def printVals(curr):
            i = 0
            while curr:
                if i == 5:
                    return
                i+=1
                print(curr.val)
                curr = curr.next
            return 
        def reverse(prev, curr, numTimes):
            savedCurr = curr

            for i in range(numTimes):
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev, savedCurr, curr

                
        # curr = head.next
        # head.next = None
        # curr = reverse(head, curr, 3)
        # printVals(curr)
        # return
        prev = None
        curr = head
        i = 1

        while i<left:
            prev = curr
            curr = curr.next
        #savedCurrNext = curr.next
        '''
        lets think this through - we need to keep track of 4 values - prev -> attach to newback. newfront -> curr.next


        '''
        newBack, newFront, curr = reverse(prev, curr, right-left+1)
        printVals(newBack)
   
        if prev is None:
            print('TRUE')
            print(newFront.val)
            
            newFront.next = curr
           # printVals(newBack)
            return newBack
        

        prev.next = newBack
        
        newFront.next = curr
        #printVals(head)
        return head


        

