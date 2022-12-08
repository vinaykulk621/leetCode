# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root,leaf):
            if root:
                if root.left==None and root.right==None:
                    leaf.append(root.val)
                traverse(root.left,leaf)
                traverse(root.right,leaf)
            return leaf
        leaf1,leaf2=[],[]
        leaf1=traverse(root1,leaf1)
        leaf2=traverse(root2,leaf2)
        return leaf1==leaf2
