from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        op = []

        stk = [root]

        while stk:
            node = stk.pop()

            op.append(node.val)

            # Push children in reverse order
            stk += reversed(node.children)

        return op