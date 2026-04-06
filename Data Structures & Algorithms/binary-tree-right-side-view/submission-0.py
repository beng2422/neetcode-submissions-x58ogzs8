# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        ret = []
        if not root:
            return []
        while stack:
            
            length = len(stack)
            ret.append(stack[length-1].val)

            for _ in range(length):
                node = stack[0]
                stack = stack[1:]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
        return ret