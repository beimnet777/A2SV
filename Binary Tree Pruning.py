# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        x=dict()
        def label(node):
            if not node:
                return
            else:
                right=label(node.right)
                left=label(node.left)
                sign=node.val==1 or right or left
                x[node]=sign
                return sign
        def helper(node):
            if not node:
                return
            else:
                if node.right and x[node.right]:
                    helper(node.right)
                else:
                    node.right=None
                if node.left and x[node.left]:
                    helper(node.left)
                else:
                    node.left=None
        label(root)
        if x[root]:
            helper(root)
            return root
