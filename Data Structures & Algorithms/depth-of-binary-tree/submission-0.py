# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursion(depth, node: Optional[TreeNode]):
            if node:
                depth += 1
                l = recursion(depth, node.left)
                r = recursion(depth, node.right)
                return max(l, r)
            else:
                return depth - 1
        return recursion(1, root)







