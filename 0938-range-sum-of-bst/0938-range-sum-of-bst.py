# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stk, sum = [root], 0
        while stk:
            node = stk.pop()
            if node:
                if node.val > L:
                    stk.append(node.left)    
                if node.val < R:
                    stk.append(node.right)
                if L <= node.val <= R:
                    sum += node.val    
        return sum