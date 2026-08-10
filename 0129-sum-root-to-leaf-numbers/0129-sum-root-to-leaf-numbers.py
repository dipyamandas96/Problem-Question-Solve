# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        def helper(root, res):
            if root.left is None and root.right is None:
                res += str(root.val)
                ans.append(int(res))
                return

            res += str(root.val)

            if root.left:
                helper(root.left, res)

            if root.right:
                helper(root.right, res)

        helper(root, "")
        return sum(ans)