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
        x = 0
        if not root:
            return 0
        while len(queue)>0:
            
            s = len(queue)
            for _ in range(s):
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            x+=1
        return x
            

            
        








