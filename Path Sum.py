# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans=[0]
        def helper(root,sumx):
            if root==None:
                return
            elif root.left ==None and root.right==None:
                if root.val==sumx:
                    ans[0]=-1
            else:
                sumx-=root.val
                helper(root.right,sumx)
                helper(root.left,sumx)
        helper(root,targetSum)
        return ans[0]==-1              
