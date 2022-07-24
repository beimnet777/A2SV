# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node,depth):
            if node==None:
                return float("inf")
            elif node.left==None and node.right==None:
                return depth+1
            else:
                left=helper(node.left,depth+1)
                right=helper(node.right,depth+1)
                return min(left,right)
        ans=helper(root,0)
        return ans if ans!=float("inf") else 0
