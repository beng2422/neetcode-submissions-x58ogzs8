# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #bfs through root until root values match. 
        #Once they match check if that node has a children equivalent to subroot
        #Another idea: iterate through root and find nodes that have same depth as subroot. 
        #Check all those subroots
        subroot_queue = [()]

        queue = [root]
        while len(queue)>0:
            node = queue.pop()
            if node.val == subRoot.val:
                root_node = node
                subroot_queue.append((root_node, subRoot))
                while len(subroot_queue)>0:
                    root_node, subroot_node = subroot_queue.pop()
                    
                    if subroot_node.val != root_node.val:
                        break
                    if subroot_node.right and root_node.right:
                        subroot_queue.append((subroot_node.right, root_node.right))
                    if subroot_node.left and root_node.left:
                        subroot_queue.append((subroot_node.left, root_node.left))
                    if subroot_node.right and not root_node.right or subroot_node.left and not root_node.left:
                        break
                    if not subroot_node.left and not  root_node.left and not  subroot_node.right and not  subroot_node.left:
                        return True
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return False
            

