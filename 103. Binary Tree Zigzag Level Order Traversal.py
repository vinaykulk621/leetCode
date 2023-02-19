# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result,queue=[],[root]
        left_to_right=True
        while queue:
            level_size,level=len(queue),[]
            for i in range(level_size):
                node=queue.pop(0)
                if left_to_right:
                    level.append(node.val)
                else:
                    level=[node.val]+level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            left_to_right=not left_to_right
        return result
