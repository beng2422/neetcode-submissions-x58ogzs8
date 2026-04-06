# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        stack = [root]
        outputlist = []
        if not root:
            return []

        while stack:
            length = len(stack)

            
            newlist = []
            for i in stack:
                newlist.append(i.val)
            outputlist.append(newlist)
            for _ in range(length):
                node = stack[0]
                stack = stack[1:]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return outputlist
