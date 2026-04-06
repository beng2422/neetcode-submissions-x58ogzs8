"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        if not node:
            return node

        def dfs(node):
            if node in clones:
                return clones[node]
            newNode = Node(node.val)
        

            clones[node] = newNode
            for i in node.neighbors:
               # if i not in seen:
                
                    newNeighb = dfs(i)
                    newNode.neighbors.append(newNeighb)

                    
            return newNode
        
        return dfs(node)