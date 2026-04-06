# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #two pointers, but I cant have a pointer moving backwards
        #what if I split it in half then reverse the second list then combine them

        #split it - find length then split
        curr = head
        n = 0
        while curr:
            n+=1
            curr = curr.next
        print('n', n)

        rightHalf = head
        #split
        for i in range(n//2):
            rightHalf = rightHalf.next
        
        print('rightHalf', rightHalf.val)
        leftHalfTail = head
        for i in range(n // 2 - 1): # Go up to the node BEFORE the split point
            leftHalfTail = leftHalfTail.next
        
        # The start of the right half is the node *after* the leftHalfTail
        rightHalf = leftHalfTail.next
        
        # !!! CRITICAL FIX: Break the link !!!
        leftHalfTail.next = None            
        #reverse:
        prev = None
        curr = rightHalf
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        print('prev', prev.val)
       # prev.next = None
        # while prev:
        #     print(prev.val)
        #     prev = prev.next

        #return
        curr = head
        rev = prev
        #just merge two arrays
        #head.next = prev, 
        
        while rev:
            next_node = head.next
            rev_next = rev.next
            curr.next = rev
            curr = curr.next
            
            if next_node is None:                 # <-- added early check
                curr.next = rev_next              # append any remaining right nodes
                break
            curr.next = next_node
            curr = curr.next
            #print('r', prev.val)
            head = next_node
  
            rev = rev_next
           # print('r', head)

            
        #return dummy








