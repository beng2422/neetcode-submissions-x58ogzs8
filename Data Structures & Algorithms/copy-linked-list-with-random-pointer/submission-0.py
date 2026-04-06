"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def printVal(node):
            while node:
                print(node.val)
                node = node.next
        array = {}
        array2 = []
        headToList = head
        i = 0
        while headToList:
            array[headToList] = i
            array2.append(headToList)
            headToList = headToList.next
            i+=1

        newList = Node(head.val)
        newListPtr = newList
        newArray = [newList]
        curr = newList
        for i in range(1, len(array)):
            
            newNode = Node(array2[i].val)
            curr.next = newNode
            curr = curr.next
            newArray.append(newNode)
        
        printVal(newList)
        

        for i in range(len(newArray)):
            if array2[i].random:
                randNodeIndex = array[array2[i].random]
            
                newList.random = newArray[randNodeIndex]
            else:
                newList.random = None
            newList = newList.next
        printVal(newListPtr)
        return newListPtr





