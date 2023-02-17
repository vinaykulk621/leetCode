# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node==None:
                return
            traverse(node.left)
            trav.append(node.val)
            traverse(node.right)
        trav,ans=[],10**5+1
        traverse(root)
        for i in range(len(trav)-1):
            ans=min(ans,abs(trav[i]-trav[i+1]))
        return ans
