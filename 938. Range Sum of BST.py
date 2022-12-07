# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root):
            nonlocal ans
            if root:
                if low<=root.val<=high:
                    ans+=root.val
                if low<root.val:
                    traverse(root.left)
                if high>root.val:
                    traverse(root.right)
        ans=0
        traverse(root)
        return ans
