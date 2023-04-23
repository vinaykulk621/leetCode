# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def trav(node,p,q):
            if p.val<node.val and q.val<node.val:
                return trav(node.left,p,q)
            elif p.val>node.val and q.val>node.val:
                return trav(node.right,p,q)
            else:
                return node
        return trav(root,p,q)
