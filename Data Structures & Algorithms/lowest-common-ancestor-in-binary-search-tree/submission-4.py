# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #hmm - my thinking here is there are 2 main components: one is did we find the val and is it a descendant of the other
        #OR does it split off at that point. 
        ret = []
        def dfs(node):
            if not node:
                return False
            print(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                print('left and right is true', node.val)
                ret.append(node)
            print('  val of left, right', left, right)
            if node.val == p.val:
                #run dfs to see if q is the descendant
                print('node is p')
                if left or right:
                    print('adding here')
                    ret.append(p)
                return True

            elif node.val == q.val: 
                print('node is q')
                if left or right:
                    print('adding below')
                    ret.append(q)
                return True

            #return dfs(node.left) or dfs(node.right)
            else:
                return left or right
        dfs(root)
        if not len(ret):
            return root
        return ret[0]






