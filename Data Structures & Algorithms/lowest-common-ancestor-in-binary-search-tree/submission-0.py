# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #What were looking for is a node where p<=node<=q or vice versa, if both are less or greater than traverse down that side
        queue = [root]
        while len(queue)>0:
            node = queue.pop()
            if p.val<= node.val and node.val<= q.val or  q.val<= node.val and node.val<= p.val:
                return node
            if p.val<node.val and q.val<node.val:
                queue.append(node.left)
            if node.val<p.val and q.val<node.val:
                queue.append(node.right)
            
        return root



        