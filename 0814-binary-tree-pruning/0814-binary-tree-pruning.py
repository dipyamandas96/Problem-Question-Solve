
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if total sum of subtree is 0 than delete that substree
        total_sum: int = self.get_sum(root)

        if total_sum == 0:
            return None
        else:
            return root

    def get_sum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        left_sum: int = self.get_sum(root.left)
        right_sum: int = self.get_sum(root.right)

        if left_sum == 0:
            root.left = None
        if right_sum == 0:
            root.right = None

        return left_sum + right_sum + root.val