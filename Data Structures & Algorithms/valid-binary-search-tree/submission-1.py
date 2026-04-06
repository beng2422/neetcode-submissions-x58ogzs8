# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = [root]
        while len(queue)>0:
            node = queue.pop()
            if node.left:
                if node.left.val>=node.val:
                    return False
                queue.append(node.left)
            if node.right:
                if node.right.val<=node.val:
                    return False
                queue.append(node.right)
        return True
                
        