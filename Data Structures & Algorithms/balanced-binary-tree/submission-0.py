# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node:
                return 0
            
            height_left = dfs(node.left)
            height_right = dfs(node.right)
            if (height_left)>height_right+1 or (height_left)<height_right-1:
                return -10000
            
            return max(height_left, height_right) + 1

        x = dfs(root)
        if x<0:
            return False
        return True