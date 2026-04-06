# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #node, high, low
        queue = [(root, 10000000, -100000)]
        while len(queue)>0:
            node, high, low = queue.pop()
            if not node:
                continue
            if node.val>=high or node.val<=low:
                return False
            queue.append((node.right, high, node.val))
            queue.append((node.left, node.val, low))
            # if node.left:
            #     if node.left.val>=node.val:
            #         return False
            #     queue.append(node.left)
            # if node.right:
            #     if node.right.val<=node.val:
            #         return False
            #     queue.append(node.right)
        return True
                
        