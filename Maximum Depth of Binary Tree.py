# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node,depth):
            if node==None:
                return depth
            else:
                left=helper(node.left,depth+1)
                right=helper(node.right,depth+1)
                return max(left,right)
        return helper(root,0)
