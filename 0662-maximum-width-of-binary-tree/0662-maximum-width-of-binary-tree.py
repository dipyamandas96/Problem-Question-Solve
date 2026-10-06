# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = deque()
        d.append((root, 0))

        maxi = 0
        while d:
            l = len(d)
            first, last = 0, 0
            for i in range(l):
                node, val = d.popleft()
                
                if i == 0:
                    first = val
                if i == l-1:
                    last = val
                
                if node.left:
                    d.append((node.left, 2*val+1))
                if node.right:
                    d.append((node.right, 2*val+2))
                
            maxi = max(maxi, (last - first + 1))

        
        return maxi