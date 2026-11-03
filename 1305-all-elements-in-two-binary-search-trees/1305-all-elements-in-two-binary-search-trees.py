# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def gen(node):
            if node:
                yield from gen(node.left)
                yield node.val
                yield from gen(node.right)
        return list(heapq.merge(gen(root1), gen(root2)))