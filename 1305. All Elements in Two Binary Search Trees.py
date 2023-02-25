# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans=[]
        def trav(node):
            if node is None:
                return
            trav(node.left)
            ans.append(node.val)
            trav(node.right)
        trav(root1)
        trav(root2)
        ans.sort()
        return ans
