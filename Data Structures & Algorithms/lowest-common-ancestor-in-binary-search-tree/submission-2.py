# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #its a bst, therefore the ancestor will be between and including p and q

        #we could do something recursive - at each level we move to the right or left depending on if its in the middle or not

        while not p.val<=root.val<=q.val:
            if p.val>root.val:
                root = root.right
            else:
                root = root.left
        return root
