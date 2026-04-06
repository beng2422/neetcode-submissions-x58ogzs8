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
                subroot_queue = [(root_node, subRoot)]
                match = True
                while subroot_queue:
                    root_node, subroot_node = subroot_queue.pop()

                    if not root_node and not subroot_node:
                        continue
                    if not root_node or not subroot_node:
                        match = False
                        break
                    if root_node.val != subroot_node.val:
                        match = False
                        break

                    subroot_queue.append((root_node.left, subroot_node.left))
                    subroot_queue.append((root_node.right, subroot_node.right))

                if match:
                    return True

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return False
            

