# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node):
            if node==None:
                return 0
            elif node.val<low:
                tot=helper(node.right)
                return tot
            elif node.val>high:
                tot=helper(node.left)
                return tot
            else:
                tot1=helper(node.right)
                tot2=helper(node.left)
                return tot1+tot2+node.val
        return helper(root) 
