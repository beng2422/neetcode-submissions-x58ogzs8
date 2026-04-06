# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not (p and q):
            return false
        stack_p = [p]
        stack_q = [q]
        while len(stack_p)>0 and len(stack_q)>0:
            node_p = stack_p.pop()
            node_q = stack_q.pop()


            if node_p.val != node_q.val:
                return False
            if node_p.left:
                stack_p.append(node_p.left)
            if node_p.right:
                stack_p.append(node_p.right)        
            if node_q.left:
                stack_q.append(node_q.left)
            if node_q.right:
                stack_q.append(node_q.right)
            if node_p.left and not node_q.left:
                return False
            if node_q.left and not node_p.left:
                return False
            if node_p.right and not node_q.right:
                return False
            if node_q.right and not node_p.right:
                return False
        return True