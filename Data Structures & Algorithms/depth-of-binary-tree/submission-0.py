# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        maxNum = 0
        x = 1
        if not root:
            return 0
        while len(queue)>0:
            node = queue.pop()
            if node.left or node.right:
                x+=1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return x
            

            
        








