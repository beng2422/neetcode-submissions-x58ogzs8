# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        def printVal(reverseList):
            print('jere')
            while reverseList:
               # print('here1', reverseList.val)
                reverseList = reverseList.next

        #find the halfval
        

        halfVal = head
        fastVal = head
        
        while fastVal and fastVal.next:
            halfVal = halfVal.next
            fastVal = fastVal.next.next
         #   if fastVal:
           #     fastVal = fastVal.next
            
       # print(halfVal.val)



        
        #reverse the halfval

        second_half = halfVal.next
        halfVal.next = None   # cut the list
        currPtr = second_half
        reverseList = None
        while currPtr:
            
            
            # nextVal = curr
            # curr.next = prev
            # curr = nextVal.next
            # prev = 

            currPtrNext = currPtr.next
            oldReverseList = reverseList
            reverseList = currPtr
            reverseList.next = oldReverseList
            currPtr =currPtrNext




      #  printVal(reverseList)
            # reverseList = 2


            # currPtr = 2468
            # reverseList --  2->None
            # currPtr = 468

            # reverseList -- 46None

        headRet = head
      #  printVal(head)
       # printVal(reverseList)
        while reverseList and head :
            print('headVal', head.val)
            if reverseList:
             print('revList', reverseList.val)
            headNext = head.next
            reverseListNext = reverseList.next
            head.next = reverseList
            if headNext:
              reverseList.next = headNext
            reverseList = reverseListNext
            head = headNext
          
      #  head.next = None
      #  print(headRet)
        printVal(headRet)

        return None



       # print(reverseList)
        