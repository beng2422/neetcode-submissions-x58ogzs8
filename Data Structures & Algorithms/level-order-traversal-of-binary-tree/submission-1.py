# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        ret = []
        while queue:
            
            ret.append([n.val for n in queue])
            process = queue
            queue = []
            for node in process:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ret

            