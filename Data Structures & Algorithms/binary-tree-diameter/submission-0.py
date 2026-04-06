# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if not node:
                return (0, 0)
            left_height, diamaterleft = dfs(node.left)
            right_height, diamaterright = dfs(node.right)
            height = max(left_height, right_height) + 1
            diameter = max(diamaterleft, diamaterright, left_height + right_height) 
            return (height, diameter)




        _, d = dfs(root)
        return d





        return 0

        # stack = [root]
        # ans = 0
        # heights = {}
        # heights[root] = 0

        # while stack:
        #     node = stack.pop()

            
        #     if node.left:
        #         stack.append(node.left)
        #         heights[node.left] = heights[node]+1
        #     if node.right:
        #         stack.append(node.right)
        #         heights[node.right] = heights[node]+1

        



        
