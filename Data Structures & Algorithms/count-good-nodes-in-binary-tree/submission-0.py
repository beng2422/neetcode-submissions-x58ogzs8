# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = [(root, root.val)]
        if not root:
            return 0
        
        ret = 0

        while stack:
            node, largestVal = stack.pop()
            if node.val>=largestVal:
                ret+=1
                largestVal = node.val
            
            if node.left:
                stack.append((node.left, largestVal))
            if node.right:
                stack.append((node.right, largestVal))
        return ret