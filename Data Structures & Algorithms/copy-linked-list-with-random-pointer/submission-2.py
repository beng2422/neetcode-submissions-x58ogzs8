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
        #copy all the nodes first, then go through it again and copy the random nodes 
        #store each node pointer in a list
        #first we need to copy which node the begnning pointer came from- maybe we can find the index?
        # we could use a dictionary to find the node with the index

        node_to_index = {}
        #first fill in node_to_index
        curr = head
        i = 0
        while curr:
            node_to_index[curr] = i
            curr = curr.next
            i+=1


        #now copy it - except the random vals
        index_to_node = {} #new dictionary
        curr = head
        #set up the prev nodes
        prevNode = Node(curr.val)
        curr = curr.next
        nextNode = None
        index_to_node[0] = prevNode
        i = 1
        firstNode= prevNode
        while curr:
            
            nextNode = Node(curr.val)
            index_to_node[i] = nextNode
            prevNode.next = nextNode
            prevNode = prevNode.next
            i+=1
            curr = curr.next
            
        
        print(index_to_node)
        print(node_to_index)
        # while firstNode:
        #     print(firstNode.val)
        #     firstNode = firstNode.next
        # return
        currNew = firstNode
        currOld = head
        while currNew:
            if currOld.random:
                index_of_rand = node_to_index[currOld.random]
                currNew.random = index_to_node[index_of_rand]
            
            currNew = currNew.next
            currOld = currOld.next
        return firstNode


        










        
