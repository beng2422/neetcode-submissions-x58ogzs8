# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def printV(node):
            val1 = node
            while val1:
                print(val1.val)
                val1 = val1.next
        
        nextVal = None 
        def reverse(node):


            curr = node
            prev = None
            i = 0
            while curr:
                print('i', i)
                next_node = curr.next
                
                
                curr.next = prev
                prev = curr
                curr = next_node
                i+=1


                if i>=k:
                    nextVal = next_node
                    return prev, node, curr
            return prev, node, curr
        
     #   prev, node, curr = reverse(head)
        def kLeft(curr):
            node = curr
            i = 0
            while i<k and node:
                node = node.next
                i+=1
                if not node and i<k:
                    return False
            return True
        curr = head
        i = 0
        mainPrev = None
        prevs = []
        nodes = []
        while curr and kLeft(curr):
            prev, node, curr = reverse(curr)
            prevs.append(prev)
            nodes.append(node)
            if i==0:
                
                mainPrev = prev
              #  node.next=curr
                
            i+=1
            node.next = curr
            printV(mainPrev)
            
        for i in prevs:
       #     print('here5235')
            printV(i)
        for i in range(len(nodes)-1):
           # print('hwer23490234')
            printV(i)
            nodes[i].next = prevs[i+1]

      #  printV(nodes[0])
    #    return prevs[0]
      #  printV(head)
     #   print('past')
     #   printV(node)
    #    print('done')
     #   printV(mainPrev)
        return mainPrev
            
